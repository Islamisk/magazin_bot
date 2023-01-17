from aiogram import types
from handlers.constans import HELP

async def peremoga(message: types.Message):
    await message.answer(text=HELP)