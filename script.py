from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from time import sleep
import os
import tweepy


load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='hardware')
async def hardware_handler(message: types.Message):
    text = "test\n"
    await message.answer(f"{text}", parse_mode=types.ParseMode.HTML)

@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    text = "test\n"
    await message.answer(f"{text}", parse_mode=types.ParseMode.HTML)

def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()