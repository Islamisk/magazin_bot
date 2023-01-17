from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def t_shirts(message: types.Message):

    await message.answer(text='Футболки:')
    await message.answer(text='Красная', reply_markup=buy_item_kb)
    await message.answer(text='Белая', reply_markup=buy_item_kb)
