import httpx

from app.api.challenge import Challenge
from app.api.event import Event


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=base_url)

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