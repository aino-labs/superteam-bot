from enum import Enum
from sys import prefix

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters.callback_data import CallbackData


class PaginatedAction(Enum):
    select = 'select'
    page = 'page'
    current = 'current'


class PaginatedCallbackBase(CallbackData, prefix='paginated'):
    action: PaginatedAction
    value: int


def get_paginated_keyboard(items: list, callback_class: type[PaginatedCallbackBase], page: int = 1, per_page: int = 5):
    keyboard = [
        [
            InlineKeyboardButton(
                text=items[i],
                callback_data=callback_class(action=PaginatedAction.select,
                                                value=i).pack()
            )
        ]
        for i in range((page - 1) * per_page, min(page * per_page, len(items)))
    ]

    total_pages = (len(items) + per_page - 1) // per_page
    if total_pages > 1:
        nav_buttons = [
            InlineKeyboardButton(
                text="⬅️",
                callback_data=callback_class(action=PaginatedAction.page,
                                                value=page - 1 if page > 1 else total_pages).pack()
            ),
            InlineKeyboardButton(
                text=f"{page}/{total_pages}",
                callback_data=callback_class(action=PaginatedAction.current,
                                                value=page).pack()
            ),
            InlineKeyboardButton(
                text="➡️",
                callback_data=callback_class(action=PaginatedAction.page,
                                                value=page + 1 if page < total_pages else 1).pack()
            ),
        ]
        keyboard.append(nav_buttons)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)