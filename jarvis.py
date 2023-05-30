from aiogram import executor
from init_jarvis import dp
from data_base import mainDB

async def on(_):
    print("Проснулся")
    mainDB.start_sqlite_db()

from handlers import client, other

other.register_handlers_other(dp)
client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on)