from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.settings import settings
from app.api import APIClient
from app.cache import cached
from app.keyboards import MenuCallback, get_paginated_keyboard, PaginatedCallbackBase, PaginatedAction


class EventsCallback(PaginatedCallbackBase, prefix='events'):
    pass


router = Router()


@cached('events')
async def get_events(user_id: int, api_client: APIClient):
    data = await api_client.get_events()
    return [(x.id, x.title) for x in data]


@router.message(Command('events'))
async def events(msg: Message, api_client: APIClient):
    events = await get_events(msg.from_user.id, api_client)
    await msg.answer('Ближайшие события:', reply_markup=get_paginated_keyboard(events, EventsCallback))


@router.callback_query(MenuCallback.filter(F.command == 'events'))
async def events_callback(callback: CallbackQuery):
    await events(callback.message)


@router.callback_query(EventsCallback.filter(F.action == PaginatedAction.page))
async def events_page_callback(callback: CallbackQuery, callback_data: EventsCallback, api_client: APIClient):
    events = await get_events(callback.from_user.id, api_client)
    await callback.message.edit_reply_markup(
        reply_markup=get_paginated_keyboard(events, EventsCallback, page=callback_data.value))


@router.callback_query(EventsCallback.filter(F.action == PaginatedAction.select))
async def events_select_callback(callback: CallbackQuery, callback_data: EventsCallback, api_client: APIClient):
    event = await api_client.get_event(callback_data.value)
    await callback.message.answer(settings.messages.event_description.format(**vars(event)))

__all__ = ['router']
