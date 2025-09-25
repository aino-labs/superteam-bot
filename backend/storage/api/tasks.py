from celery import shared_task
import httpx
from urllib.parse import urljoin

from config import env
from events.models import Event
from competitions.models import Competition
from datetime import datetime

MAX_RETRIES = 5
RETRY_DELAY = 60


@shared_task(bind=True, max_retries=MAX_RETRIES)
def fetch_events(self):
    """Fetch events from API and update DB with retry on failure."""
    try:
        base_url = urljoin(env.env_required('EVENTS_API_URL'), 'calendar/get')
        with httpx.Client() as client:
            response = client.get(base_url, params={'api_id': env.env_required('EVENTS_FEED_ID')})
            response.raise_for_status()
            data = response.json()
        for item in data['featured_items']:
            event = item['event']
            Event.objects.update_or_create(
                api_id=event['api_id'],
                defaults={
                    'title': event['name'],
                    'location': event['geo_address_info']['address'],
                    'event_date': datetime.strptime(event['start_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                    'source_url': urljoin(env.env_required('EVENTS_SHARE_URL'), event['url'])
                }
            )
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
            response = client.get(env.env_required('CHALLENGES_API_URL'))
            response.raise_for_status()
            data = response.json()
        for item in data:
            Competition.objects.update_or_create(
                api_id=item['id'],
                defaults={
                    'title': item['title'],
                    'prize': item['rewardAmount'],
                    'deadline': datetime.strptime(item['deadline'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                    'source_url': urljoin(env.env_required('CHALLENGES_SHARE_URL'), item['slug'])
                }
            )
    except httpx.RequestError as e:
        print(f"Error fetching data: {e}")
        raise self.retry(countdown=RETRY_DELAY, exc=e)
    except Exception as e:
        print(f"Error updating data: {e}")
        raise self.retry(countdown=RETRY_DELAY, exc=e)

