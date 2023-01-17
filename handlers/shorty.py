from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def shorts(message: types.Message):

    await message.answer(text='Шорты:')
    await message.answer(text='Красные', reply_markup=buy_item_kb)
    await message.answer(text='Белые', reply_markup=buy_item_kb)