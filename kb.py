from telebot.types import InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup


def main_menu():
    k = ReplyKeyboardMarkup(resize_keyboard=True)
    k.add(KeyboardButton("Buy proxy"),KeyboardButton("Account"))
    k.add(KeyboardButton("FAQ"))
    return k

def account_buttons(id):
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton('Donate', callback_data='donate_'+id))
    k.add(InlineKeyboardButton('My pays', callback_data='pays_' + id))
    k.add(InlineKeyboardButton('Refferal system', callback_data='refferal_' + id))
    k.add(InlineKeyboardButton('Close', callback_data='close_account'))