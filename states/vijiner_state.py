from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class Vijiner(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    plain_text = State() # ism
    plain_key = State() # email


class deVijiner(StatesGroup):
    cipher_text = State()
    key = State()