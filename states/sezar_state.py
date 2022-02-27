from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class Sezar(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    plain_text = State() # ism
    key = State() # email


class deSezar(StatesGroup):
    shifr_matn = State()
    key = State()