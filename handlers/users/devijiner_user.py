from aiogram.types import Message

from keyboards.default.allbuttons import devijimenu, shifrmenu, menu
from utils.vijiner_shifr import decrypt
from aiogram.dispatcher import FSMContext

from loader import dp
from states.vijiner_state import deVijiner


@dp.message_handler(text_contains="Bosh")
async def first(message: Message):
    await message.answer('Shifrlash/Deshifrlash usulini tanlang',reply_markup=menu)

@dp.message_handler(text_contains = "Orqaga🔙")
async def back(message: Message):
    await message.answer('Deshifrlash usulini tanlang',reply_markup=shifrmenu)

@dp.message_handler(text= 'Vijiner deshifrlash usuli haqidaℹ️')
async def about(message: Message):
    await message.answer("<a href='https://google.com/Vijiner'>Vijiner deshifrlash usuli</a>")

# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text_contains = "Vijiner deshifrlash usuli")
@dp.message_handler(text_contains = "(deVijiner)")
async def enter_test(message: Message):
    await message.answer("Shifrlangan matn kiriting")
    await deVijiner.cipher_text.set()


@dp.message_handler(state=deVijiner.cipher_text)
async def get_text(message: Message, state: FSMContext):
    cipher_text = message.text.lower()
    cipher_text = cipher_text.replace(" ","")
    if not cipher_text.isalpha():
        await message.answer("Faqat xarflardan iborat matn kiriting!")
        await state.reset_data()
    else:
        await state.update_data(
            {"text": cipher_text}
        )

        await message.answer("Kalitni kiriting <b>(so'z kiritilsin)</b>")

    # await PersonalData.email.set()
        await deVijiner.next()

@dp.message_handler(state=deVijiner.key)
async def get_key(message: Message, state: FSMContext):
    key = message.text.lower()
    key = key.rstrip()
    if not key.isalpha():
        await message.answer("Kaltini to'g'ri kiriting. Kalit xarflardan iborat matn bo'lishi kerak!")

    else:
        await state.update_data(
            {"key": key}
        )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    text = data.get("text")
    key = data.get("key")

    msg = f"Shifrlangan matn -> {text}\n"
    msg += f"Kalit -> {key}\n\n"
    msg += f"Matn: - {decrypt(text,key)}"
    await message.answer(msg,reply_markup=devijimenu)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()