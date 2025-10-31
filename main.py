import telebot
import random

#1828269322
bot = telebot.TeleBot("7972631102:AAEClRjTSYfKWlO0v-FXkh5g_lYpG9kWYJQ")

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_MoreVideosDownload = telebot.types.KeyboardButton(text="🎬 Скачать: MoreVideosDownload ▶️")
button_support = telebot.types.KeyboardButton(text="💻 Написать в поддержку: 💬")
keyboard.add(button_MoreVideosDownload)
keyboard.add(button_support)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "👋 Вас приветствует бот-Toxan4ik, я помогу вам🤝 разобраться с вашими проблемами в программах💻 и скачать эти самые программы! 🤙")
    bot.send_sticker(message.chat.id, random.choice(["CAACAgIAAxkBAAEO7tJodhsGeX8ihJZB9MAZeRWMqD1vOgACwBEAAmcaoErrkdFHd0JoDDYE", "CAACAgIAAxkBAAEO7tRodhsfO1FHLFdlGgF5W-Ac-IygqAACnBEAAlrm2UoljQp-E1bV5TYE"]), reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: "support_otvet" in call.data)
def support_otvetdef(call):
    message = call.message
    chat_id_to = str(call.data).replace("support_otvet_","")
    chat_id = message.chat.id
    keyboard_reset = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_reset = telebot.types.KeyboardButton(text="Отмена:❌")
    keyboard_reset.add(button_reset)
    msg = bot.send_message(chat_id, "❗ Ответ от поддержки: ❗", reply_markup=keyboard_reset)
    bot.register_next_step_handler(msg, input_support_otvet, chat_id_to)

def input_support_otvet(message, chat_id_to):
    msg = message.text
    if str(msg).replace(" ","") != "Отмена:❌":
        bot.send_message(message.chat.id, f"❗ Вы отправили данное сообщение от лица поддержки: ❗\n\n{msg}", reply_markup=keyboard)
        bot.send_message(chat_id_to, f"❗ Ответ от поддержки: ❗\n\n{msg}")
    else:
         bot.send_message(message.chat.id, "Вы отменили отправку сообщения от лица поддержки!", reply_markup=keyboard)

def input_promocod(message):
    msg = message.text
    if str(msg).replace(" ","") != "Отмена:❌":
        keyboard_inline = telebot.types.InlineKeyboardMarkup()
        button_otvet = telebot.types.InlineKeyboardButton(text="👁‍🗨 Ответить: 💬", callback_data=f"support_otvet_{message.from_user.id}")
        keyboard_inline.add(button_otvet)
        bot.send_message(1828269322, f"❗ ЖАЛОБА: ❗\n\n🆔: {message.from_user.id}\nИмя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}\nНик: {message.from_user.username}\nЯзыковой код: {message.from_user.language_code}\n\n{msg}", reply_markup=keyboard_inline)
        bot.send_message(message.chat.id, "Мы отправили вашу жалобу на рассмотрение в поддержку!", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Вы отменили отправку сообщения в поддержку!", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "🎬 Скачать: MoreVideosDownload ▶️")
def MoreVideosDownload_download(message):
    keyboard_inline = telebot.types.InlineKeyboardMarkup()
    button_zip = telebot.types.InlineKeyboardButton(text="Скачать в zip:", url="https://drive.google.com/file/d/1WPvWKSmmNy-TRcmePahBH6tlLLA2Z497/view")
    button_rar = telebot.types.InlineKeyboardButton(text="Скачать в rar:", url="https://drive.google.com/file/d/1WP0zfAd_kbZJAP5WIbNPQx0iINKPK4sx/view")
    keyboard_inline.add(button_zip, button_rar)
    bot.send_message(message.chat.id, text='Скачать программу "MoreVideosDownload" в разных форматах:', reply_markup=keyboard_inline)

@bot.message_handler(func=lambda message: message.text == "💻 Написать в поддержку: 💬")
def Support_write(message):
    keyboard_reset = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_reset = telebot.types.KeyboardButton(text="Отмена:❌")
    keyboard_reset.add(button_reset)
    msg = bot.send_message(message.chat.id, f"🧐 Конечно мы выслушаем вас. Пожалуйста, подробно опишите свою проблему текстом 🤔:", reply_markup=keyboard_reset)
    bot.register_next_step_handler(msg, input_promocod)

bot.polling(none_stop=True)