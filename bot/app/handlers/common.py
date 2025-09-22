from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.settings import settings

router = Router()


@router.message(Command('start'))
async def start(msg: Message):
    await msg.answer(settings.messages.start)


@router.message(Command('privacy'))
async def privacy(msg: Message):
    await msg.answer(settings.messages.privacy)


@router.message(Command('menu'))
async def menu(msg: Message):
    pass


__all__ = ['router']
