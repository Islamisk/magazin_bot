from aiogram import types
from handlers.constans import bad


async def check_message(message: types.Message):
    """
    проверка на плохие слова
    """
    BAD_WORDS = ["stupid", "dumb"]
    if message.chat.type != 'private':
        for word in BAD_WORDS:
            if message.text.lower().replace(' ', '').count(word):
                await message.reply(
                    text=bad.format(
                        first_name=message.from_user.first_name
                    ))
                break


async def ban_user(message: types.Message):
    """
    обработчик для бана
    """
    if message.chat.type != 'private':
        admins = await message.chat.get_administrators()
        for admin in admins:
            if admin["user"]["id"] == message.from_user.id:
                print(f"{admin=}")
                if admin and message.reply_to_message:
                    await message.bot.ban_chat_member(
                        chat_id=message.chat.id,
                        user_id=message.reply_to_message.from_user.id
                    )