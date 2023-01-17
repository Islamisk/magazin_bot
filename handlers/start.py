from aiogram import types
from handlers.constans import start_text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(
    InlineKeyboardButton('Магазин', callback_data='shop_start'),
    InlineKeyboardButton('Адрес магазина', callback_data='shop_adress')
)


async def start_command(message: types.Message):
    await message.answer(
        text=start_text.format(first_name=message.from_user.first_name),
        reply_markup=start_kb
    )