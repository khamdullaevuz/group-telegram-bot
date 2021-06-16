import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ChatType

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

@dp.message_handler(chat_type=ChatType.PRIVATE)
async def send_welcome(message: types.Message):
	if message.text == "/start":
		await message.reply("Salom men guruhlarda ishlovchi botman!", reply_markup=main_keyboard)

@dp.message_handler(chat_type=[ChatType.SUPERGROUP, ChatType.GROUP])
async def send_welcome(message: types.Message):
	if message.text == "/start@ChatSettingsBot":
		await message.reply("Men guruhda ishlashim uchun admin berishingiz kerak!")

backbutton = InlineKeyboardButton('Ortga', callback_data="back")
back_keyboard = InlineKeyboardMarkup()
back_keyboard.add(backbutton)

@dp.callback_query_handler(text='commands')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    text = 'Bot buyruqlari:\n/start - qayta ishga tushirish'

    await bot.edit_message_text(text, query.from_user.id, query.message.message_id, reply_markup=back_keyboard)

@dp.callback_query_handler(text='back')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    text = 'Salom men guruhlarda ishlovchi botman!'

    await bot.edit_message_text(text, query.from_user.id, query.message.message_id, reply_markup=main_keyboard)

@dp.message_handler(content_types=["new_chat_member"])
async def handler_new_member(message):
    first_name = message.new_chat_member.first_name
    await bot.send_message(message.chat.id, "ok")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)