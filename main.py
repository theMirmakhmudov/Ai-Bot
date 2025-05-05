import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from services.data import get_data

TOKEN = "Your Token"

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"*Assalomu Aleykum, Xurmatli {message.from_user.full_name}*")


@dp.message()
async def question(message: types.Message):
    question_text = message.text
    answer_text = get_data(question_text)
    await message.answer(f"*{answer_text}*")


async def main() -> None:
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
