from fastapi import FastAPI, Request, Header, HTTPException
from app import bot, api_client
from app.api import Event
from app.config import config

app = FastAPI()

@app.post('/notify')
async def receive_event(request: Request, Authorization: str = Header(None)):
    if Authorization != config.webhook_token:
        raise HTTPException(status_code=403, detail="Invalid token")
    event_data = await request.json()
    event = Event(**event_data)

    users = await api_client.get_subscribers()
    for chat_id in users:
        await bot.send_message(chat_id, f"Новое событие!: {event.title}")

    return {"status": "success"}