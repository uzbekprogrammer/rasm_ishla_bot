import asyncio
import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            send = await dp.bot.send_message(admin, "🤩Bot ishga tushdi🤩")
            # await asyncio.sleep(5)
            # await send.delete()
        except Exception as err:
            logging.exception(err)

