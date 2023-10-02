import asyncio
import logging
import sys
from os import getenv, environ as env

from aiogram import Bot, Router, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from utils import messageType,parseCategories

try:
    from setEnvironment import setVariables
    setVariables()
except:
    print('''Error: You need to make ./setEnvironment.py with setVariables function.
           This function has to set os.environ["TG_TOKEN"] and os.environ["MONGO_CONNECT_TOKEN"]''')
    sys.exit(1)

print('TG_TOKEN' in env)
from mongoDB import connect
connect()

TOKEN = env['TG_TOKEN']
dp = Dispatcher()

@dp.message(CommandStart())
async def commands_start_bot(message: Message) -> None:
    await message.answer(f"{message.from_user.full_name}, Chirik, epta!\n I hope you know what is purpose of this bote. Please write me the message with categories")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode = ParseMode.HTML)
    await dp.start_polling(bot)


@dp.message()
async def echo_handler(message: types.Message) -> None:
    if (messageType(message.text) == 'categories'):
        await message.answer(f"You have got next categories: {', '.join(parseCategories(message.text))}")
    else:
        try:
            # Send a copy of the received message
            await message.send_copy(chat_id=message.chat.id)
        except TypeError:
            # But not all the types is supported to be copied so need to handle it
            await message.answer("Nice try!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())