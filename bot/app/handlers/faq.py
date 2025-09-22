from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from app.keyboards import get_paginated_keyboard, PaginatedCallbackBase, PaginatedAction, MenuCallback

from app.settings import settings
from app.ai import LLMService

router = Router()

class FaqCallback(PaginatedCallbackBase, prefix='faq'):
    pass


@router.message(Command('faq'))
async def faq(msg: Message):
    await msg.answer('Выберите вопрос:',
                     reply_markup=get_paginated_keyboard(settings.faq, FaqCallback))


@router.callback_query(MenuCallback.filter(F.command == 'faq'))
async def faq_callback(callback: CallbackQuery):
    await faq(callback.message)


@router.callback_query(FaqCallback.filter(F.action == PaginatedAction.page))
async def faq_page_callback(callback: CallbackQuery, callback_data: FaqCallback):
    await callback.message.edit_reply_markup(
        reply_markup=get_paginated_keyboard(settings.faq, FaqCallback, page=callback_data.value))


@router.callback_query(FaqCallback.filter(F.action == PaginatedAction.select))
async def faq_page_callback(callback: CallbackQuery, callback_data: FaqCallback, llm_service: LLMService):
    response = await llm_service.ask(settings.faq[callback_data.value])
    await callback.message.answer(response)


__all__ = ['router']
