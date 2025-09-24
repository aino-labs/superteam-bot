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
        return [Challenge(**el) for el in resp.json()['results']]

    async def get_events(self) -> list[Event]:
        resp = await self.client.get('/events/')
        resp.raise_for_status()
        return [Event(**el) for el in resp.json()['results']]