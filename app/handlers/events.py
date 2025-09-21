from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('events'))
async def start(msg: Message):
    pass

__all__ = ['router']
