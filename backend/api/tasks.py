from celery import shared_task
import httpx
from django.forms.models import model_to_dict

from config import env
from django.utils import timezone
from events.models import Event
from competitions.models import Competition
from datetime import datetime
from urllib.parse import urljoin

MAX_RETRIES = 5
RETRY_DELAY = 60


@shared_task(bind=True, max_retries=MAX_RETRIES)
def fetch_events(self):
    """Fetch events from API and update DB with retry on failure."""
    try:
        with httpx.Client() as client:
            response = client.get(urljoin(env.env_required("EVENTS_API_URL"), '/calendar/get'),
                                  params={'api_id': env.env_required('EVENTS_FEED_ID')})
            response.raise_for_status()
            data = response.json()
        new_data = []
        for item in data["featured_items"]:
            event = item["event"]
            event_new, created = Event.objects.update_or_create(
                api_id=event["api_id"],
                defaults={
                    "title": event["name"],
                    "location": event["geo_address_info"]["address"],
                    "event_date": datetime.strptime(
                        event["start_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    "source_url": urljoin(env.env_required("EVENTS_SHARE_URL"), event["url"]),
                },
            )
            if created:
                print('event is new')
                event_data = model_to_dict(event_new)
                event_data['event_date'] = event_data['event_date'].isoformat()
                new_data.append(event_data)
        # fire webhook
        if new_data:
            send_event_webhook.delay(new_data)
    except httpx.RequestError as e:
        print(f"Error fetching data: {e}")
        raise self.retry(countdown=RETRY_DELAY, exc=e)
    except Exception as e:
        print(f"Error updating data: {e}")
        raise self.retry(countdown=RETRY_DELAY, exc=e)


@shared_task(bind=True, max_retries=MAX_RETRIES)
def fetch_challenges(self):
    """Fetch challenges from API and update DB with retry on failure."""
    try:
        with httpx.Client() as client:
            response = client.get(env.env_required("CHALLENGES_API_URL"))
            response.raise_for_status()
            data = response.json()
        new_data = []
        for item in data:
            competition, created = Competition.objects.update_or_create(
                api_id=item["id"],
                defaults={
                    "title": item["title"],
                    "prize": item["rewardAmount"],
                    "deadline": datetime.strptime(
                        item["deadline"], "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                },
            )

    except httpx.RequestError as e:
        print(f"Error fetching data: {e}")
        raise self.retry(countdown=RETRY_DELAY, exc=e)
    except Exception as e:
        print(f"Error updating data: {e}")
        raise self.retry(countdown=RETRY_DELAY, exc=e)


@shared_task
def cleanup_expired_events_and_challenges():
    """
    Deletes events and challenges whose dates have already passed.
    Scheduled to run every 30 minutes via Celery Beat.
    """
    try:
        now = timezone.now()

        Event.objects.filter(event_date__lt=now).delete()
        Competition.objects.filter(deadline__lt=now).delete()
    except Exception as e:
        print(f"Error delete data: {e}")


@shared_task(bind=True, max_retries=5, default_retry_delay=60)
def send_event_webhook(self, event_data: list[Event]):
    try:
        with httpx.Client() as client:
            response = client.post(env.env_required('WEBHOOK_URL'),
                                   json=event_data,
                                   timeout=10,
                                   headers={'Authorization': env.env_required('WEBHOOK_TOKEN')})
            response.raise_for_status()
            print(f"Notification sent for {len(event_data)} events")
    except httpx.RequestError as e:
        print(f"Failed to send notification for {len(event_data)} events: {e}")
        self.retry(exc=e)
