from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.api import APIClient
from app.cache import cached
from app.keyboards import MenuCallback, PaginatedCallbackBase, get_paginated_keyboard, PaginatedAction
from app.settings import settings
from app.utils import fmt_date

router = Router()


class ChallengesCallback(PaginatedCallbackBase, prefix='challenges'):
    pass


@cached('challenges')
async def get_challenges(user_id: int, api_client: APIClient):
    data = await api_client.get_challenges()
    return [(x.id, x.title) for x in data]


@router.message(Command('challenges'))
async def challenges(msg: Message, api_client: APIClient):
    events = await get_challenges(msg.from_user.id, api_client)
    await msg.answer('Доступные соревнования:', reply_markup=get_paginated_keyboard(events, ChallengesCallback))


@router.callback_query(MenuCallback.filter(F.command == 'challenges'))
async def challenges_callback(callback: CallbackQuery, api_client: APIClient):
    await challenges(callback.message, api_client)


@router.callback_query(ChallengesCallback.filter(F.action == PaginatedAction.page))
async def challenges_page_callback(callback: CallbackQuery, callback_data: ChallengesCallback, api_client: APIClient):
    events = await get_challenges(callback.from_user.id, api_client)
    await callback.message.edit_reply_markup(
        reply_markup=get_paginated_keyboard(events, ChallengesCallback, page=callback_data.value))


@router.callback_query(ChallengesCallback.filter(F.action == PaginatedAction.select))
async def challenges_select_callback(callback: CallbackQuery, callback_data: ChallengesCallback, api_client: APIClient):
    challenge = await api_client.get_challenge(callback_data.value)
    await callback.message.answer(settings.messages.challenge_description.format(
        **{**vars(challenge), **{'deadline': fmt_date(challenge.deadline)}}))

__all__ = ['router']
