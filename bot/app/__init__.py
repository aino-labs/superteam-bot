import logging
from typing import Any, Callable
from aiogram import Bot, Dispatcher, BaseMiddleware
from aiogram.client.default import DefaultBotProperties
from aiogram.types import TelegramObject

from app.api import APIClient
from app.config import config
from app.settings import settings
from app.ai import LLMService
from app.handlers import common_router, faq_router, events_router, challenges_router, subscription_router



bot = Bot(config.bot_token, default=DefaultBotProperties(parse_mode='HTML'))

dp = Dispatcher()
dp['llm_service'] = LLMService(config.llm.api_key, config.llm.base_url)
dp['api_client'] = APIClient(config.api_url)

dp.include_routers(
    common_router,
    faq_router,
    events_router,
    challenges_router,
    subscription_router
)
