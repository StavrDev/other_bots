from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('Курс криптовалют', callback_data='crypto')
button2 = InlineKeyboardButton('Курс валют', callback_data='currency')
keyboard.add(button1, button2)

kb_cur = InlineKeyboardMarkup(row_width=1)
btn_back = InlineKeyboardButton("Назад", callback_data="back")
btn_update_cur = InlineKeyboardButton("Обновить", callback_data='update_cur')
kb_cur.add(btn_update_cur,btn_back)

kb_crypto = InlineKeyboardMarkup(row_width=1)
btn_back = InlineKeyboardButton("Назад", callback_data="back")
btn_update_crypto = InlineKeyboardButton("Обновить", callback_data='update_crypto')
kb_crypto.add(btn_update_crypto,btn_back)