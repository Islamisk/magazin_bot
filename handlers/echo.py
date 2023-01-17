from aiogram import types

async def echo(message: types.Message):
    if len(message.text.split()) >= 3:
        await message.reply(text=message.text.upper())
    else:
        await message.answer("yes")