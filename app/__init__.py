import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.config import config
from app.settings import settings
from app.handlers import common_router, faq_router, events_router, challenges_router, subscription_router


bot = Bot(config.bot_token, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
dp.include_routers(
    common_router,
    faq_router,
    events_router,
    challenges_router,
    subscription_router
)
