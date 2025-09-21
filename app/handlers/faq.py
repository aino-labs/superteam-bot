from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters.callback_data import CallbackData

from app.settings import settings

router = Router()


class FaqCallback(CallbackData, prefix="faq"):
    action: str
    value: int


def get_questions_keyboard(questions: list, page: int = 1, per_page: int = 5):
    keyboard = [
        [
            InlineKeyboardButton(
                text=questions[i],
                callback_data=FaqCallback(action='ask', value=i).pack()
            )
        ]
        for i in range((page - 1) * per_page,min(page * per_page, len(questions)))
    ]

    total_pages = (len(questions) + per_page - 1) // per_page
    if total_pages > 1:
        nav_buttons = [
            InlineKeyboardButton(
                text="⬅️",
                callback_data=FaqCallback(action='page', value=page - 1 if page > 1 else total_pages).pack()
            ),
            InlineKeyboardButton(
                text=f"{page}/{total_pages}",
                callback_data=FaqCallback(action='current', value=page).pack()
            ),
            InlineKeyboardButton(
                text="➡️",
                callback_data=FaqCallback(action='page', value=page + 1 if page < total_pages else 1).pack()
            ),
        ]
        keyboard.append(nav_buttons)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


@router.message(Command('faq'))
async def start(msg: Message):
    await msg.answer('Выберите вопрос:',
                     reply_markup=get_questions_keyboard(settings.faq))


@router.callback_query(FaqCallback.filter(F.action == 'page'))
async def faq_page_callback(callback: CallbackQuery, callback_data=FaqCallback):
    await callback.message.edit_reply_markup(
        reply_markup=get_questions_keyboard(settings.faq, page=callback_data.value))


@router.callback_query(FaqCallback.filter(F.action == 'ask'))
async def faq_page_callback(callback: CallbackQuery, callback_data=FaqCallback):
    pass


__all__ = ['router']
