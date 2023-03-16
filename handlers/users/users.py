from aiogram import Dispatcher
from aiogram.types import *

from keyboards.inline.users_btn import languages_btn
from loader import dp
from utils.misc.text_translator import text_trans
from database.connections import add_user



async def bot_start(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await add_user(user_id, user_name)
    await message.answer(f"Salom")


async def help_bot(message: Message):
    await message.answer("Bu botda siz:\n\n"
                         "3 xil tilda 🌐 yozgan so'zingizni tarjima\n"
                         "qilib beradi ✅ va bu botda adminlar uchun"
                         "alohida panel mavjud ✅ unda admin,\n"
                         "bot userlariga malomot yuborishi\n"
                         "mumkin ✅ lekin adminladan boshqalariga\n"
                         "esa /admin commandasi ishlamaydi\n"
                         "Bot setlari:\n"
                         "                   /start\n"
                         "                   /admin\n"
                         "                   /help")


async def get_user_text_handler(message: Message):
    text = message.text
    btn = await languages_btn()
    await message.answer(text, reply_markup=btn)


async def select_lang_callback(call: CallbackQuery):
    await call.answer()
    lang = call.data.split(":")[-1]
    context = call.message.text
    result = await text_trans(context, lang)
    if context != result:
        btn = await languages_btn()
        await call.message.edit_text(result, reply_markup=btn)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(help_bot, commands=['help'])
    dp.register_message_handler(get_user_text_handler, content_types=['text'])

    dp.register_callback_query_handler(select_lang_callback, text_contains='lang:')
