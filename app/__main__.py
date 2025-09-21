import asyncio
import logging

from app import bot, dp
from app.utils import setup_logging
from app.config import config


async def main():
    setup_logging(config.log_level, config.logging_path)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())