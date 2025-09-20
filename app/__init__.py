from aiogram import Bot, Dispatcher
from app.config import config

bot = Bot(config.bot_token)
dp = Dispatcher()