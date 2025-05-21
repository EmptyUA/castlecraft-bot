import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Получаем токен из переменной окружения
API_TOKEN = os.getenv("BOT_TOKEN")
if not API_TOKEN or " " in API_TOKEN or not API_TOKEN.startswith("726"):
    raise ValueError("❌ BOT_TOKEN is missing or malformed. Double-check the token!")

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer_photo(
        photo=InputFile("castle.jpg"),
        caption="🏰 Welcome to CastleCraft!"
    )
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("My Castle", "Missions")
    keyboard.add("Balance", "Boosts")
    await message.answer("Choose an option:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "My Castle")
async def my_castle(message: types.Message):
    await message.answer_photo(
        photo=InputFile("my_castle.jpg"),
        caption="🏯 This is your level 1 Castle!"
    )

@dp.message_handler(lambda message: message.text == "Missions")
async def missions(message: types.Message):
    await message.answer_photo(
        photo=InputFile("missions.jpg"),
        caption="⚔️ Arena Challenge:"

Who built the first castle?

A) Romans
B) Knights
C) Egyptians"
    

@dp.message_handler(lambda message: message.text == "Balance")
async def balance(message: types.Message):
    await message.answer_photo(
        photo=InputFile("balance.jpg"),
        caption="💰 Your balance:
CASL: 120
Gold: 540"
    )

@dp.message_handler(lambda message: message.text == "Boosts")
async def boosts(message: types.Message):
    await message.answer_photo(
        photo=InputFile("boosts.jpg"),
        caption="🪙 Tap the CASL coin to boost earnings!"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
