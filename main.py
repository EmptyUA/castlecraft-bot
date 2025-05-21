import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = "YOUR_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню
def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("My Castle", callback_data="my_castle"),
        InlineKeyboardButton("Missions", callback_data="missions"),
        InlineKeyboardButton("Balance", callback_data="balance"),
        InlineKeyboardButton("Boosts", callback_data="boosts")
    )
    return keyboard

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    photo = types.InputFile("castle.jpg")
    await message.answer_photo(photo=photo, caption="🏰 Welcome to CastleCraft 🏰\nLoading...", parse_mode="HTML")
    await message.answer("Choose your path:", reply_markup=main_menu())

@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    action = callback_query.data
    if action == "my_castle":
        photo = types.InputFile("my_castle.jpg")
        await bot.send_photo(callback_query.from_user.id, photo, caption="🏰 Your Castle — Level 1")
    elif action == "missions":
        photo = types.InputFile("missions.jpg")
        await bot.send_photo(callback_query.from_user.id, photo, caption="⚔️ Arena of Knowledge\n\nWhat is the capital of the medieval kingdom?\n\nA) Avalon\nB) Camelot\nC) Eldoria")
    elif action == "balance":
        photo = types.InputFile("balance.jpg")
        await bot.send_photo(callback_query.from_user.id, photo, caption="💰 Balance:\nCASL: 120\nGold: 540")
    elif action == "boosts":
        photo = types.InputFile("boosts.jpg")
        await bot.send_photo(callback_query.from_user.id, photo, caption="🪙 Tap the coin to earn CASL!")
    await bot.answer_callback_query(callback_query.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
