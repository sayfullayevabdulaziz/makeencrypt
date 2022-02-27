from aiogram.types import Message

from keyboards.default.allbuttons import sezarmenu, shifrmenu, menu
from utils.sezar_shifr import cipher_encrypt
from aiogram.dispatcher import FSMContext

from loader import dp
from states.sezar_state import Sezar

@dp.message_handler(text_contains="Bosh")
async def first(message: Message):
    await message.answer('Shifrlash/Deshifrlash usulini tanlang',reply_markup=menu)

@dp.message_handler(text = "🔙Orqaga")
async def back(message: Message):
    await message.answer('Shifrlash usulini tanlang',reply_markup=shifrmenu)

@dp.message_handler(text_contains= 'Sezar shifrlash usuli haqida')
async def about(message: Message):
    await message.answer("<a href='https://google.com'>Sezar shifrlash usuli</a>")

# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text_contains = "SEZAR")
@dp.message_handler(text = "♻️Davom ettirish(Sezar)")
async def enter_test(message: Message):
    await message.answer("Matn kiriting")
    await Sezar.plain_text.set()


@dp.message_handler(state=Sezar.plain_text)
async def get_text(message: Message, state: FSMContext):
    plain_text = message.text

    await state.update_data(
        {"text": plain_text}
    )

    await message.answer("Kalitni kiriting <b>(sonda kiritilsin)</b>")

    # await PersonalData.email.set()
    await Sezar.next()

@dp.message_handler(state=Sezar.key)
async def get_key(message: Message, state: FSMContext):
    key = message.text
    if not key.isdigit():
        await message.answer('Son kiriting')
        await state.reset_data()
    else:
        await state.update_data(
        {"key": int(key)}
    )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    text = data.get("text")
    key = data.get("key")

    msg = f"Matn -> {text}\n"
    msg += f"Kalit -> {key}\n\n"
    msg += f"Shifrlangan matn: - {cipher_encrypt(text,key)}"
    await message.answer(msg,reply_markup=sezarmenu)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()