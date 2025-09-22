from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.keyboards import MenuCallback

router = Router()

@router.message(Command('events'))
async def events(msg: Message):
    pass

@router.callback_query(MenuCallback.filter(F.command == 'events'))
async def events_callback(callback: CallbackQuery):
    await events(callback.message)

__all__ = ['router']
