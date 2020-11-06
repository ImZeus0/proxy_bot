import telebot
import config
import kb
import db


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    registration(m.chat.id,m.from_user.username)


@bot.message_handler(content_types=['text'])
def main_menu(m):
    if m.text == 'Buy proxy':
        pass
    elif m.text == 'Account':
        pass
    elif m.text == 'FAQ':
        pass

def text_account(id,balance,count_pays,sum_donate,date_registraion):
    text = '<b>ID:</b> '+id+'\n'
    text += '<b>BALANCE:</b> ' + balance + '\n'
    text += '<b>COUNT PAYS:</b> ' + count_pays + '\n'
    text += '<b>SUM DONATE:</b> ' + sum_donate + '\n'
    text += '<b>DATE REGISTRATOIN:</b> ' + date_registraion + '\n'

def registration(id,nickname):
    c = db.connect()
    users = db.select_users(c)
    check = False
    for user in users:
        if user['id_user'] == id:
            check = True
    if check == False:
        db.add_user(c,id,nickname)
        bot.send_message(id, 'You register ' + nickname, reply_markup=kb.main_menu())
    else:
        bot.send_message(id,'Hello '+nickname,reply_markup=kb.main_menu())



bot.polling()