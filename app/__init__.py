import logging


from aiogram import Bot, Dispatcher
from app.config import config
from app.settings import settings


bot = Bot(config.bot_token)
dp = Dispatcher()

