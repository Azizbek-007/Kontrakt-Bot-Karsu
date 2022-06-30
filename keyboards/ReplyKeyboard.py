from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def main_btn():
    btn1 = KeyboardButton(text='🔄 To`lemler')
    btn2 = KeyboardButton(text='⛔️ Shig\'iw')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    return markup