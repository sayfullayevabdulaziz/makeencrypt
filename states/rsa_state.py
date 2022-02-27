from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class Rsa(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    p = State() # ism
    q = State() # email
    plain_text = State() # email

class deRsa(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    dp = State() # ism
    dq = State()
    private_key = State()# email
    cipher_text = State() # email
