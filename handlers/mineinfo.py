from aiogram import types
from handlers.constans import myinfo


async def moya_infa(message: types.Message):

    await message.answer(text=myinfo.format(
        id={message.from_user.id},
        Name={message.from_user.first_name},
        LastName={message.from_user.last_name})
    )
