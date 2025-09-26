from fastapi import FastAPI, Request, Header, HTTPException
from app import bot, api_client, settings
from app.api import Event
from app.cache import cached
from app.config import config
from app.keyboards import get_paginated_keyboard
from app.handlers.events import EventsCallback

app = FastAPI()


@cached('events', True)
async def cache_events(user_id: int, events: list[Event]):
    return [(x.id, f'{x.title} - {x.event_date.strftime("%d.%m.%Y")}') for x in events]


@app.post('/notify')
async def receive_event(request: Request, Authorization: str = Header(None)):
    if Authorization != config.webhook_token:
        raise HTTPException(status_code=403, detail="Invalid token")
    event_data = await request.json()
    events = [Event(**x) for x in event_data]

    users = await api_client.get_subscribers()
    for chat_id in users:
        cached_events = await cache_events(chat_id, events)
        await bot.send_message(chat_id,
                               settings.messages.notification.format(title='• ' + '\n• '.join([x.title for x in events])),
                               reply_markup=get_paginated_keyboard(cached_events, EventsCallback))

    return {"status": "success"}