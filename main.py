from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.help import peremoga
from handlers.echo import echo
from handlers.pictures import picture
from handlers.mineinfo import moya_infa
from handlers.start import start_command
from handlers.adress import magazin_adress
from handlers.magazin import shop_start
from handlers.futbolki import t_shirts
from handlers.shorty import shorts

load_dotenv()
bot = Bot(getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


dp.register_message_handler(shorts, text='шорты')
dp.register_message_handler(t_shirts, text="футболки")
dp.register_callback_query_handler(shop_start, text='shop_start')
dp.register_callback_query_handler(magazin_adress, text='magazin_adress')
dp.register_message_handler(start_command, commands="start")
dp.register_message_handler(moya_infa, commands="myinfo")
dp.register_message_handler(peremoga, commands="help")
dp.register_message_handler(picture, commands="picture")
dp.register_message_handler(echo)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)