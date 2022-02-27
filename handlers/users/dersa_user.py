import sympy
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from keyboards.default.allbuttons import deshifrmenu, dersa_menu, menu
from utils.dersa_shifr import *
from loader import dp
from states.rsa_state import deRsa

@dp.message_handler(text_contains="Bosh")
async def first(message: Message):
    await message.answer('Shifrlash/Deshifrlash usulini tanlang',reply_markup=menu)


@dp.message_handler(text = "Orqaga🔙")
async def back(message: Message):
    await message.answer('Deshifrlash usulini tanlang',reply_markup=deshifrmenu)

@dp.message_handler(text = 'Rsa deshifrlash usuli haqidaℹ️')
async def about(message: Message):
    await message.answer("<a href='https://google.com/RSA'>Rsa deshifrlash usuli</a>")


@dp.message_handler(text_contains = "Rsa deshifrlash usuli")
@dp.message_handler(text_contains = "(deRsa)")
async def enter_test(message: Message):
    await message.answer("p = <b>(Tub son kiriting)</b>")
    await deRsa.dp.set()


@dp.message_handler(state=deRsa.dp)
async def answer_p(message: Message, state: FSMContext):
    p = int(message.text)
    if not sympy.isprime(p):
        await message.answer("P tub son emas!\nTub son kiriting")
        await state.reset_data()
    else:
        await state.update_data(
            {"p": p}
        )

        await message.answer("q = <b>(Tub son kiriting)</b>")

        # await PersonalData.email.set()
        await deRsa.next()

@dp.message_handler(state=deRsa.dq)
async def answer_q(message: Message, state: FSMContext):
    q = int(message.text)
    if not sympy.isprime(q):
        await message.answer("Q tub son emas!\nTub son kiriting")

    else:
        await state.update_data(
            {"q": q}
        )

        await message.answer("Yopiq kalitni(PrivateKey) kiriting")

        await deRsa.next()


@dp.message_handler(state=deRsa.private_key)
async def answer_plain_text(message: Message, state: FSMContext):
    private_key = int(message.text)

    await state.update_data(
        {"p_k": private_key}
    )

    await message.answer("Shifrlangan matnni kiriting")
    await deRsa.next()

@dp.message_handler(state=deRsa.cipher_text)
async def ciphe_text(message: Message, state: FSMContext):
    cipher_text = message.text
    a = cipher_text.replace('[', '')
    b = a.replace(']', '')
    c = list(b.split(','))
    await state.update_data(
        {"cip_k":c}
    )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    p = data.get("p")
    q = data.get("q")
    d = data.get("p_k")
    cip_k = data.get("cip_k")
    n = p * q
    privateKey = (d, n)

    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f"p -> {p}\n"
    msg += f"q -> {q}\n"
    msg += f"Shifrlangan matn -> {cip_k}\n"
    msg += f"Private Key ( d= {d}, n= {n})\n\n"
    msg += f"Matn ->{RSA(p,q,d,cip_k)}"
    await message.answer(msg,reply_markup=dersa_menu)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()