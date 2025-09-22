from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.settings import settings
from app.keyboards import get_menu_keyboard, MenuCallback

router = Router()


@router.message(Command('start'))
async def start(msg: Message):
    await msg.answer(settings.messages.start)


@router.message(Command('privacy'))
async def privacy(msg: Message):
    await msg.answer(settings.messages.privacy)


@router.callback_query(MenuCallback.filter(F.command == 'privacy'))
async def privacy_callback(callback: CallbackQuery):
    await privacy(callback.message)


@router.message(Command('menu'))
async def menu(msg: Message):
    await msg.answer('Быстрые команды:', reply_markup=get_menu_keyboard())


__all__ = ['router']
