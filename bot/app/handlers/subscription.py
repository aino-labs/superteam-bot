from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app import APIClient
from app.keyboards import MenuCallback

router = Router()

@router.message(Command('subscribe'))
async def subscribe(msg: Message, api_client: APIClient):
    await api_client.add_subscriber(msg.from_user.id)
    await msg.answer('Вы подписаны на новые события!')


@router.callback_query(MenuCallback.filter(F.command == 'subscribe'))
async def subscribe_callback(callback: CallbackQuery, api_client: APIClient):
    await subscribe(callback.message, api_client)


@router.message(Command('unsubscribe'))
async def unsubscribe(msg: Message):
    pass


@router.callback_query(MenuCallback.filter(F.command == 'unsubscribe'))
async def unsubscribe_callback(callback: CallbackQuery):
    await unsubscribe(callback.message)


__all__ = ['router']
