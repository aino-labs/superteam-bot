from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('subscribe'))
async def start(msg: Message):
    pass


@router.message(Command('unsubscribe'))
async def start(msg: Message):
    pass


__all__ = ['router']
