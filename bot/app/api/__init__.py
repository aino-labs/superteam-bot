
import httpx

from app.api.challenge import Challenge
from app.api.event import Event
from app.config import config


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=base_url,
                                        headers={'Authorization': 'Token ' + config.api_token})

    async def get_challenges(self) -> list[Challenge]:
        resp = await self.client.get('/competitions/')
        resp.raise_for_status()
        data = [Challenge(**el) for el in resp.json()['results']]
        data.sort(key=lambda x: x.deadline)
        return data

    async def get_challenge(self, challenge_id: int) -> Challenge:
        resp = await self.client.get(f'/competitions/{challenge_id}/')
        resp.raise_for_status()
        return Challenge(**resp.json())

    async def get_events(self) -> list[Event]:
        resp = await self.client.get('/events/')
        resp.raise_for_status()
        data =[Event(**el) for el in resp.json()['results']]
        data.sort(key=lambda x: x.event_date)
        return data

    async def get_event(self, event_id: int) -> Event:
        resp = await self.client.get(f'/events/{event_id}/')
        resp.raise_for_status()
        return Event(**resp.json())

    async def get_subscribers(self):
        resp = await self.client.get('/subscribes/')
        resp.raise_for_status()
        return [x['chat_id'] for x in resp.json()['results']]

    async def add_subscriber(self, user_id: int):
        resp = await self.client.post('/subscribes/', data={
            'chat_id': str(user_id) # TODO: fix
        })
        resp.raise_for_status()

    async def remove_subscriber(self, user_id: int):
        resp = await self.client.delete(f'/subscribes/{user_id}/')
        resp.raise_for_status()