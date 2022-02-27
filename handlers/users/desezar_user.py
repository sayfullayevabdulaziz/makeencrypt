from aiogram.types import Message

from keyboards.default.allbuttons import desezarmenu, menu, deshifrmenu
from utils.sezar_shifr import cipher_decrypt
from aiogram.dispatcher import FSMContext

from loader import dp
from states.sezar_state import deSezar

@dp.message_handler(text_contains="Bosh")
async def first(message: Message):
    await message.answer('Shifrlash/Deshifrlash usulini tanlang',reply_markup=menu)

@dp.message_handler(text = "Orqaga🔙")
async def back(message: Message):
    await message.answer('Deshifrlash usulini tanlang',reply_markup=deshifrmenu)

@dp.message_handler(text= 'Sezar deshifrlash usuli haqidaℹ️')
async def about(message: Message):
    await message.answer("<a href='https://google.com/sezar'>Sezar deshifrlash usuli</a>")

# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text = "Sezar deshifrlash usuli")
@dp.message_handler(text_contains = "(deSezar)")
async def enter_test(message: Message):
    await message.answer("Shifrlangan matn kiriting")
    await deSezar.shifr_matn.set()


@dp.message_handler(state=deSezar.shifr_matn)
async def get_text(message: Message, state: FSMContext):
    shifr_matn = message.text

    await state.update_data(
        {"text": shifr_matn}
    )

    await message.answer("Kalitni kiriting <b>(sonda kiritilsin)</b>")

    # await PersonalData.email.set()
    await deSezar.next()

@dp.message_handler(state=deSezar.key)
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

    msg = f"Shifrlangan matn -> {text}\n"
    msg += f"Kalit -> {key}\n\n"
    msg += f"Deshifrlangan matn: - {cipher_decrypt(text,key)}"
    await message.answer(msg,reply_markup=desezarmenu)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()