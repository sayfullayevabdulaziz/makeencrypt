from aiogram import types

from keyboards.default.allbuttons import shifrmenu, deshifrmenu
from loader import dp


@dp.message_handler(text_contains="Shifrlash")
async def bot_echo(message: types.Message):
    await message.answer('Shifrlash usulini tanlang',reply_markup=shifrmenu)

@dp.message_handler(text_contains="Deshifrlash")
async def bot_echo(message: types.Message):
    await message.answer('Deshifrlash usulini tanlang',reply_markup=deshifrmenu)
