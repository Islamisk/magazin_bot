from aiogram import types


async def magazin_adress(cb: types.CallbackQuery):
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Пушкина 5',
    )