from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot = Bot(getenv("BOT_TOKEN"))

dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start_hendler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}")


@dp.message_handler(commands=["help"])
async def peremoga(message: types.Message):
    await message.answer(f"""/start - старт программы
                             /help - перемога
                             /myinfo - информация о себе
                             /picture - картинка""")


@dp.message_handler(commands=["myinfo"])
async def start_hendler(message: types.Message):

    await message.answer(f'''
id: {message.from_user.id}
Name: {message.from_user.first_name}
Last Name: {message.from_user.last_name}''')


@dp.message_handler(commands=["picture"])
async def start_hendler(message: types.Message):
    await message.answer_photo(
        open('./images/pep.jpg', 'rb'),
        caption='Ajax pep'
    )


@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) >= 3:
        await bot.send_message(message.from_user.id, message.text.upper())
    else:
        await message.answer("yes")


if __name__ == '__main__':
    executor.start_polling(dp)