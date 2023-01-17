from aiogram import types

async def picture(message: types.Message):
    await message.answer_photo(
        open('./images/pep.jpg', 'rb'),
        caption='Ajax pep'
    )