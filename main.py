import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🏰 My Castle"), KeyboardButton("🎯 Missions"))
menu.add(KeyboardButton("💎 Boosts"), KeyboardButton("💰 Balance"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "🏰 Welcome to *CastleCraft*!\n\nBuild your medieval empire, earn CASL tokens, and unlock historical castles.",
        parse_mode="Markdown",
        reply_markup=menu
    )

@dp.message_handler(lambda message: message.text == "🏰 My Castle")
async def show_castle(message: types.Message):
    await message.reply_photo(
        photo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Castle_Neuschwanstein.jpg/640px-Castle_Neuschwanstein.jpg",
        caption="This is your castle. Upgrade it by completing missions and using CASL boosts! 🏰"
    )

@dp.message_handler(lambda message: message.text == "🎯 Missions")
async def show_missions(message: types.Message):
    await message.reply("🎯 *Missions coming soon!* You'll fight in historical battles to earn gold and upgrade your castle.", parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "💎 Boosts")
async def show_boosts(message: types.Message):
    await message.reply("💎 Use CASL tokens to speed up your upgrades and gain special bonuses!")

@dp.message_handler(lambda message: message.text == "💰 Balance")
async def show_balance(message: types.Message):
    await message.reply("💰 Gold: 120\n🪙 CASL: 35 (demo mode)")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
