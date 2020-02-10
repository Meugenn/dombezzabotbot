import telebot
import const
import utilities
from texts import texts
import re

bot = telebot.TeleBot(const.bot_token)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, texts["main"],
                     parse_mode="HTML", reply_markup=utilities.main_markup(),
                     disable_web_page_preview=True)


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def asks_handler(call):
    n = None
    if call.data.isdigit():
        n = int(call.data)
    if not n:
        return
    ims = utilities.get_imgs(n)
    mess = []
    for i in ims:
        m = bot.send_media_group(call.message.chat.id, i)
        for i in m:
            mess.append(i.message_id)
    bot.edit_message_text(texts[n], call.from_user.id, call.message.message_id, reply_markup=utilities.back_markup(mess),
                          parse_mode="HTML")
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: re.match('back', call.data))
def back(call):
    bot.answer_callback_query(call.id)
    bot.edit_message_text(texts["main"], call.from_user.id, call.message.message_id, parse_mode="HTML", reply_markup=utilities.main_markup(),
                          disable_web_page_preview=True)
    if len(call.data) != len('back'):
        message_ids = call.data.split('_')[1:]
        for m_id in message_ids:
            if m_id.isdigit() or m_id[1:]:
                m_id = int(m_id)
            bot.delete_message(call.message.chat.id, m_id)


bot.polling(none_stop=True)
