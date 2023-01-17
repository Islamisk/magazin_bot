from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton('футболки'),
    KeyboardButton('шорты'),
)


async def shop_start(cb: types.CallbackQuery):


    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Какой товар интересует?',
        reply_markup=shop_kb
    )