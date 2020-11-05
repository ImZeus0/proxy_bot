import telebot
import config
import kb


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,str(m.chat.id),reply_markup=kb.main_menu())


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



bot.polling()