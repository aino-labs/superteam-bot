from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.keyboards import MenuCallback

router = Router()

@router.message(Command('subscribe'))
async def subscribe(msg: Message):
    pass


@router.callback_query(MenuCallback.filter(F.command == 'subscibe'))
async def subscribe_callback(callback: CallbackQuery):
    await subscribe(callback.message)


@router.message(Command('unsubscribe'))
async def unsubscribe(msg: Message):
    pass


@router.callback_query(MenuCallback.filter(F.command == 'unsubscibe'))
async def unsubscribe_callback(callback: CallbackQuery):
    await unsubscribe(callback.message)


__all__ = ['router']
