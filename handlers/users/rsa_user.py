import sympy
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from keyboards.default.allbuttons import shifrmenu, rsa_menu, menu
from utils.rsa_shifr import *
from loader import dp
from states.rsa_state import Rsa

@dp.message_handler(text_contains="Bosh")
async def first(message: Message):
    await message.answer('Shifrlash/Deshifrlash usulini tanlang',reply_markup=menu)


@dp.message_handler(text = "🔙Orqaga")
async def back(message: Message):
    await message.answer('Shifrlash usulini tanlang',reply_markup=shifrmenu)

@dp.message_handler(text_contains = 'Rsa shifrlash usuli haqida')
async def about(message: Message):
    await message.answer("<a href='https://google.com/RSA'>Rsa shifrlash usuli</a>")


@dp.message_handler(text_contains = "RSA")
@dp.message_handler(text = "♻️Davom ettirish(Rsa)")
async def enter_test(message: Message):
    await message.answer("p = <b>(Tub son kiriting)</b>")
    await Rsa.p.set()


@dp.message_handler(state=Rsa.p)
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
        await Rsa.next()

@dp.message_handler(state=Rsa.q)
async def answer_q(message: Message, state: FSMContext):
    q = int(message.text)
    if not sympy.isprime(q):
        await message.answer("Q tub son emas!\nTub son kiriting")

    else:
        await state.update_data(
            {"q": q}
        )

        await message.answer("Matn kiriting")

        await Rsa.next()


@dp.message_handler(state=Rsa.plain_text)
async def answer_plain_text(message: Message, state: FSMContext):
    plain_text = message.text

    await state.update_data(
        {"text": plain_text}
    )
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    p = data.get("p")
    q = data.get("q")
    plain_text = data.get("text")
    n = p * q
    t = (p - 1) * (q - 1)
    e = calc_e(t)
    d = calc_d(t, e)
    publicKey = (e, n)

    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f"p -> {p}\n"
    msg += f"q -> {q}\n"
    msg += f"Matn -> {plain_text}\n"
    msg += f"Public Key ( e= {e} , n= {n})\n"
    msg += f"Private Key ( d= {d}, n= {n})\n\n"
    msg += f"Shifrlangan matn ->{RSA(p,q,plain_text)}"
    await message.answer(msg,reply_markup=rsa_menu)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()