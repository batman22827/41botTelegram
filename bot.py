# Подключаем модуль случайных чисел
import random
import datetime
# Подключаем модуль для Телеграма
import telebot
import xlrd, xlwt
dict_sample1 = {
  "5А": "Понедельник: Русский, Математика , Физ-ра ",
  "6А": "Понедельник: География Физика",
  "7А": "Понедельник: История,Технология"
}
#понедельник




# Указываем токен

bot = telebot.TeleBot('1201504985:AAGMYqDdtcvzHVKwvEE-62Jh3v97yUGGp3w')

# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

# Заготовки для трёх предложений



# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я могу сказать, какие у тебя сегодня уроки.")
        bot.send_message(message.from_user.id, "Напиши свой класс, вместе с буквой (Например 5А) ")
    if message.text == "5А" or message.text == "5 А" or message.text == "5а" or message.text == "5 а":
        x = dict_sample1["5А"]
        print(x)




        bot.send_message(message.from_user.id, x)
        day = datetime.datetime.today().weekday()
    if message.text == "6А" or message.text == "6 А" or message.text == "6а" or message.text == "6 а":
        x = dict_sample1["6А"]
        print(x)
        bot.send_message(message.from_user.id, x)
        day = datetime.datetime.today().weekday()






















    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")




#

bot.polling(none_stop=True, interval=0)
