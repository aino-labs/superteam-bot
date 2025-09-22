from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from app.keyboards import get_paginated_keyboard, PaginatedCallbackBase, PaginatedAction

from app.settings import settings

router = Router()

class FaqCallback(PaginatedCallbackBase, prefix='faq'):
    pass


@router.message(Command('faq'))
async def start(msg: Message):
    await msg.answer('Выберите вопрос:',
                     reply_markup=get_paginated_keyboard(settings.faq, FaqCallback))


@router.callback_query(FaqCallback.filter(F.action == PaginatedAction.page))
async def faq_page_callback(callback: CallbackQuery, callback_data=PaginatedCallbackBase):
    await callback.message.edit_reply_markup(
        reply_markup=get_paginated_keyboard(settings.faq, FaqCallback, page=callback_data.value))


@router.callback_query(FaqCallback.filter(F.action == PaginatedAction.select))
async def faq_page_callback(callback: CallbackQuery, callback_data=FaqCallback):
    pass


__all__ = ['router']
