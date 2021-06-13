import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '1805310908:AAFe_G34KTXHhlkeM4EYRiLDf4Sry6MHlNI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

button1 = InlineKeyboardButton('Guruhga qo\'shish!', url="https://t.me/ChatSettingsBot?startgroup=new")
button2 = InlineKeyboardButton('Buyruqlar', callback_data="commands")

main_keyboard = InlineKeyboardMarkup()
main_keyboard.add(button1, button2)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    await message.reply("Salom men guruhlarda ishlovchi botman!", reply_markup=main_keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)