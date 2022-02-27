from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="🔒Shifrlash"),
         KeyboardButton(text="🔓Deshifrlash"),]
    ],resize_keyboard=True
)


shifrmenu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='SEZAR shifrlash usuli'),
         KeyboardButton(text='VIJINER shifrlash usuli'),
         ],
        [KeyboardButton(text='RSA shifrlash usuli'),
         KeyboardButton(text='GAMMA shifrlash usuli'),
         ]
    ],resize_keyboard=True
)

deshifrmenu = ReplyKeyboardMarkup([
        [KeyboardButton(text='Sezar deshifrlash usuli'),
         KeyboardButton(text='Vijiner deshifrlash usuli'),
         ],

        [KeyboardButton(text='Rsa deshifrlash usuli'),
         KeyboardButton(text='Gamma deshifrlash usuli'),
         ]
],resize_keyboard=True)

sezarmenu = ReplyKeyboardMarkup([
    [KeyboardButton(text='♻️Davom ettirish(Sezar)'),
     KeyboardButton(text='ℹ️Sezar shifrlash usuli haqida'),
    ],
    [KeyboardButton(text="🔙Orqaga"),
     KeyboardButton(text = "Bosh sahifa"),],
],resize_keyboard=True)

vijimenu = ReplyKeyboardMarkup([
    [KeyboardButton(text='♻️Davom ettirish(Vijiner)'),
     KeyboardButton(text='ℹ️Vijiner shifrlash usuli haqida'),
     ],
    [KeyboardButton(text="🔙Orqaga"),
     KeyboardButton(text = "Bosh sahifa"),],
],resize_keyboard=True)

rsa_menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='♻️Davom ettirish(Rsa)'),
         KeyboardButton(text='ℹ️Rsa shifrlash usuli haqida'),
        ],
        [KeyboardButton(text="🔙Orqaga"),
         KeyboardButton(text = "Bosh sahifa"),
        ],
    ],resize_keyboard=True
)

desezarmenu = ReplyKeyboardMarkup([
    [KeyboardButton(text='Davom ettirish(deSezar)♻️'),
     KeyboardButton(text= 'Sezar deshifrlash usuli haqidaℹ️'),
    ],
    [KeyboardButton(text="Orqaga🔙"),
     KeyboardButton(text = "Bosh sahifa"),],
],resize_keyboard=True)

devijimenu = ReplyKeyboardMarkup([
    [KeyboardButton(text='Davom ettirish(deVijiner)♻️'),
     KeyboardButton(text='Vijiner deshifrlash usuli haqidaℹ️'),
     ],
    [KeyboardButton(text="Orqaga🔙"),
     KeyboardButton(text = "Bosh sahifa"),],
],resize_keyboard=True)

dersa_menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Davom ettirish(deRsa)♻️'),
         KeyboardButton(text='Rsa deshifrlash usuli haqidaℹ️'),
        ],
        [KeyboardButton(text="Orqaga🔙"),
         KeyboardButton(text = "Bosh sahifa"),
        ],
    ],resize_keyboard=True
)