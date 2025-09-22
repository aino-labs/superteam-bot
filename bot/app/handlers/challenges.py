from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.keyboards import MenuCallback

router = Router()

@router.message(Command('challenges'))
async def challenges(msg: Message):
    pass


@router.callback_query(MenuCallback.filter(F.command == 'challenges'))
async def challenges_callback(callback: CallbackQuery):
    await challenges(callback.message)

__all__ = ['router']
