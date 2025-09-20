import asyncio
import logging

from app import bot, dp
from app.utils import setup_logging


async def main():
    setup_logging()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())