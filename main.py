import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

# Логирование
logging.basicConfig(level=logging.INFO)

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    photo = InputFile("castle.jpg")
    await message.answer_photo(
        photo,
        caption="🏰 Добро пожаловать в CastleCraft!\nПострой своё королевство и войди в историю!"
    )

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
