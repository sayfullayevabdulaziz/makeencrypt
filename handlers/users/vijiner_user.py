from aiogram.types import Message

from keyboards.default.allbuttons import vijimenu, shifrmenu, menu
from utils.vijiner_shifr import encrypt
from aiogram.dispatcher import FSMContext

from loader import dp
from states.vijiner_state import Vijiner


@dp.message_handler(text_contains="Bosh")
async def first(message: Message):
    await message.answer('Shifrlash/Deshifrlash usulini tanlang',reply_markup=menu)

@dp.message_handler(text = "🔙Orqaga")
async def back(message: Message):
    await message.answer('Shifrlash usulini tanlang',reply_markup=shifrmenu)

@dp.message_handler(text_contains= 'Vijiner shifrlash usuli haqida')
async def about(message: Message):
    await message.answer("<a href='https://google.com/Vijiner'>Vijiner shifrlash usuli</a>")

# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text_contains = "VIJINER")
@dp.message_handler(text = "♻️Davom ettirish(Vijiner)")
async def enter_test(message: Message):
    await message.answer("Matn kiriting")
    await Vijiner.plain_text.set()


@dp.message_handler(state=Vijiner.plain_text)
async def get_text(message: Message, state: FSMContext):
    plain_text = message.text.lower()
    plain_text = plain_text.replace(" ","")
    if not plain_text.isalpha():
        await message.answer("Faqat xarflardan iborat matn kiriting!")
        await state.reset_data()
    else:
        await state.update_data(
            {"text": plain_text}
        )

        await message.answer("Kalitni kiriting <b>(so'z kiritilsin)</b>")

    # await PersonalData.email.set()
        await Vijiner.next()

@dp.message_handler(state=Vijiner.plain_key)
async def get_key(message: Message, state: FSMContext):
    plain_key = message.text.lower()
    plain_key = plain_key.rstrip()
    if not plain_key.isalpha():
        await message.answer("Kaltini to'g'ri kiriting. Kalit xarflardan iborat matn bo'lishi kerak!")

    else:
        await state.update_data(
            {"plain_key": plain_key}
        )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    text = data.get("text")
    key = data.get("plain_key")

    msg = f"Matn -> {text}\n"
    msg += f"Kalit -> {key}\n\n"
    msg += f"Shifrlangan matn: - {encrypt(text,key)}"
    await message.answer(msg,reply_markup=vijimenu)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()