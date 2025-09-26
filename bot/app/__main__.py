import asyncio
import uvicorn
from app.webhooks import app
from app import bot, dp
from app.utils import setup_logging
from app.config import config


async def start_bot():
    setup_logging(config.log_level, config.logging_path)
    await dp.start_polling(bot)


async def start_listener():
    config = uvicorn.Config(app,
                            host='0.0.0.0',
                            port=7632,
                            loop='asyncio')
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    await asyncio.gather(
        start_bot(),
        start_listener()
    )


if __name__ == "__main__":
    asyncio.run(main())
