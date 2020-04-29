# Подключаем модуль случайных чисел
import random
import datetime
# Подключаем модуль для Телеграма
import telebot
import xlrd, xlwt
import openpyxl

# читаем excel-файл
day = datetime.datetime.today().weekday()

wb = openpyxl.load_workbook('ponedelnik_02_03_2020.xlsx')

# печатаем список листов
sheets = wb.sheetnames

# получаем активный лист
sheet = wb.active

from telebot import types

#################################5А#################################################
yrok5A_1 = (len(str(sheet['B2'].value)))
yrok5A_2 = (len(str(sheet['B4'].value)))
yrok5A_3 = (len(str(sheet['B6'].value)))
yrok5A_4 = (len(str(sheet['B8'].value)))
yrok5A_5 = (len(str(sheet['B10'].value)))
yrok5A_6 = (len(str(sheet['B12'].value)))
yrok5A_7 = ((len(str(sheet['B14'].value))))

# 1урок
if (yrok5A_1 > 1):
    yrok5A_1 = ("1 урок: " + str(sheet['B2'].value + ", " + "кабинет: ") + str(sheet['B3'].value) + '\n')
else:
    yrok5A_1 = ""

# 2урок
if (yrok5A_2 > 1):
    yrok5A_2 = ("2 урок: " + str(sheet['B4'].value + ", " + "кабинет: ") + str(sheet['B5'].value) + '\n')
else:
    yrok5A_2 = ""

# 3урок
if (yrok5A_3 > 1):
    yrok5A_3 = ("3 урок: " + str(sheet['B6'].value + ", " + "кабинет: ") + str(sheet['B7'].value) + '\n')
else:
    yrok5A_3 = ""

# 4урок
if (yrok5A_4 > 1):
    yrok5A_4 = ("4 урок: " + str(sheet['B8'].value + ", " + "кабинет: ") + str(sheet['B9'].value) + '\n')
else:
    yrok5A_4 = ""

# 5урок
if yrok5A_5 > 1:
    yrok5A_5 = ("5 урок: " + str(sheet['B10'].value + ", " + "кабинет: ") + str(sheet['B11'].value) + '\n')
else:
    yrok5A_5 = ""
# 6урок
if (yrok5A_6 > 1):
    yrok5A_6 = ("6 урок: " + str(sheet['B12'].value + ", " + "кабинет: ") + str(sheet['B13'].value) + '\n')
else:
    yrok5A_6 = ""
# 7урок
if (yrok5A_7 > 1):
    yrok5A_7 = ("7 урок: " + str(sheet['B14'].value + ", " + "кабинет: ") + str(sheet['B15'].value) + '\n')
else:
    yrok5A_7 = ""
# все уроки
yrok5A = yrok5A_1 + yrok5A_2 + yrok5A_3 + yrok5A_4 + yrok5A_5 + yrok5A_6 + yrok5A_7
###################################################################################


#################################5Б#################################################
yrok5B_1 = (len(str(sheet['C2'].value)))
yrok5B_2 = (len(str(sheet['C4'].value)))
yrok5B_3 = (len(str(sheet['C6'].value)))
yrok5B_4 = (len(str(sheet['C8'].value)))
yrok5B_5 = (len(str(sheet['C10'].value)))
yrok5B_6 = (len(str(sheet['C12'].value)))
yrok5B_7 = ((len(str(sheet['C14'].value))))

# 1урок
if (yrok5B_1 > 1):
    yrok5B_1 = ("1 урок: " + str(sheet['C2'].value + ", " + "кабинет: ") + str(sheet['C3'].value) + '\n')
else:
    yrok5B_1 = ""

# 2урок
if (yrok5B_2 > 1):
    yrok5B_2 = ("2 урок: " + str(sheet['C4'].value + ", " + "кабинет: ") + str(sheet['C5'].value) + '\n')
else:
    yrok5B_2 = ""

# 3урок
if (yrok5B_3 > 1):
    yrok5B_3 = ("3 урок: " + str(sheet['C6'].value + ", " + "кабинет: ") + str(sheet['C7'].value) + '\n')
else:
    yrok5B_3 = ""

# 4урок
if (yrok5B_4 > 1):
    yrok5B_4 = ("4 урок: " + str(sheet['C8'].value + ", " + "кабинет: ") + str(sheet['C9'].value) + '\n')
else:
    yrok5B_4 = ""

# 5урок
if (yrok5B_5 > 1):
    yrok5B_5 = ("5 урок: " + str(sheet['C10'].value + ", " + "кабинет: ") + str(sheet['C11'].value) + '\n')
else:
    yrok5B_5 = ""
# 6урок
if (yrok5B_6 > 1):
    yrok5B_6 = ("6 урок: " + str(sheet['C12'].value + ", " + "кабинет: ") + str(sheet['C13'].value) + '\n')
else:
    yrok5B_6 = ""
# 7урок
if (yrok5B_7 > 1):
    yrok5B_7 = ("7 урок: " + str(sheet['C14'].value + ", " + "кабинет: ") + str(sheet['C15'].value) + '\n')
else:
    yrok5B_7 = ""
# все уроки
yrok5B = yrok5B_1 + yrok5B_2 + yrok5B_3 + yrok5B_4 + yrok5B_5 + yrok5B_6 + yrok5B_7
###################################################################################


#################################5V#################################################
yrok5V_1 = (len(str(sheet['D2'].value)))
yrok5V_2 = (len(str(sheet['D4'].value)))
yrok5V_3 = (len(str(sheet['D6'].value)))
yrok5V_4 = (len(str(sheet['D8'].value)))
yrok5V_5 = (len(str(sheet['D10'].value)))
yrok5V_6 = (len(str(sheet['D12'].value)))
yrok5V_7 = ((len(str(sheet['D14'].value))))

# 1урок
if (yrok5V_1 > 1):
    yrok5V_1 = ("1 урок: " + str(sheet['D2'].value + ", " + "кабинет: ") + str(sheet['C3'].value) + '\n')
else:
    yrok5V_1 = ""

# 2урок
if (yrok5V_2 > 1):
    yrok5V_2 = ("2 урок: " + str(sheet['D4'].value + ", " + "кабинет: ") + str(sheet['D5'].value) + '\n')
else:
    yrok5V_2 = ""

# 3урок
if (yrok5V_3 > 1):
    yrok5V_3 = ("3 урок: " + str(sheet['D6'].value + ", " + "кабинет: ") + str(sheet['D7'].value) + '\n')
else:
    yrok5V_3 = ""

# 4урок
if (yrok5V_4 > 1):
    yrok5V_4 = ("4 урок: " + str(sheet['D8'].value + ", " + "кабинет: ") + str(sheet['D9'].value) + '\n')
else:
    yrok5V_4 = ""

# 5урок
if (yrok5V_5 > 1):
    yrok5V_5 = ("5 урок: " + str(sheet['D10'].value + ", " + "кабинет: ") + str(sheet['D11'].value) + '\n')
else:
    yrok5V_5 = ""
# 6урок
if (yrok5V_6 > 1):
    yrok5V_6 = ("6 урок: " + str(sheet['D12'].value + ", " + "кабинет: ") + str(sheet['D13'].value) + '\n')
else:
    yrok5V_6 = ""
# 7урок
if (yrok5V_7 > 1):
    yrok5V_7 = ("7 урок: " + str(sheet['D14'].value + ", " + "кабинет: ") + str(sheet['D15'].value) + '\n')
else:
    yrok5V_7 = ""
# все уроки
yrok5V = yrok5V_1 + yrok5V_2 + yrok5V_3 + yrok5V_4 + yrok5V_5 + yrok5V_6 + yrok5V_7
###################################################################################


#################################5G#################################################
yrok5G_1 = (len(str(sheet['E2'].value)))
yrok5G_2 = (len(str(sheet['E4'].value)))
yrok5G_3 = (len(str(sheet['E6'].value)))
yrok5G_4 = (len(str(sheet['E8'].value)))
yrok5G_5 = (len(str(sheet['E10'].value)))
yrok5G_6 = (len(str(sheet['E12'].value)))
yrok5G_7 = ((len(str(sheet['E14'].value))))

# 1урок
if (yrok5G_1 > 1):
    yrok5G_1 = ("1 урок: " + str(sheet['E2'].value + ", " + "кабинет: ") + str(sheet['E3'].value) + '\n')
else:
    yrok5G_1 = ""

# 2урок
if (yrok5G_2 > 1):
    yrok5G_2 = ("2 урок: " + str(sheet['E4'].value + ", " + "кабинет: ") + str(sheet['E5'].value) + '\n')
else:
    yrok5G_2 = ""

# 3урок
if (yrok5G_3 > 1):
    yrok5G_3 = ("3 урок: " + str(sheet['E6'].value + ", " + "кабинет: ") + str(sheet['E7'].value) + '\n')
else:
    yrok5G_3 = ""

# 4урок
if (yrok5G_4 > 1):
    yrok5G_4 = ("4 урок: " + str(sheet['E8'].value + ", " + "кабинет: ") + str(sheet['E9'].value) + '\n')
else:
    yrok5G_4 = ""

# 5урок
if (yrok5G_5 > 1):
    yrok5G_5 = ("5 урок: " + str(sheet['E10'].value + ", " + "кабинет: ") + str(sheet['E11'].value) + '\n')
else:
    yrok5G_5 = ""
# 6урок
if (yrok5G_6 > 1):
    yrok5G_6 = ("6 урок: " + str(sheet['E12'].value + ", " + "кабинет: ") + str(sheet['E13'].value) + '\n')
else:
    yrok5G_6 = ""
# 7урок
if (yrok5G_7 > 1):
    yrok5G_7 = ("7 урок: " + str(sheet['E14'].value + ", " + "кабинет: ") + str(sheet['E15'].value) + '\n')
else:
    yrok5G_7 = ""
# все уроки
yrok5G = yrok5G_1 + yrok5G_2 + yrok5G_3 + yrok5G_4 + yrok5G_5 + yrok5G_6 + yrok5G_7
###################################################################################


#################################6A#################################################
yrok6A_1 = (len(str(sheet['F2'].value)))
yrok6A_2 = (len(str(sheet['F4'].value)))
yrok6A_3 = (len(str(sheet['F6'].value)))
yrok6A_4 = (len(str(sheet['F8'].value)))
yrok6A_5 = (len(str(sheet['F10'].value)))
yrok6A_6 = (len(str(sheet['F12'].value)))
yrok6A_7 = ((len(str(sheet['F14'].value))))

# 1урок
if (yrok6A_1 > 1):
    yrok6A_1 = ("1 урок: " + str(sheet['F2'].value + ", " + "кабинет: ") + str(sheet['F3'].value) + '\n')
else:
    yrok6A_1 = ""

# 2урок
if (yrok6A_2 > 1):
    yrok6A_2 = ("2 урок: " + str(sheet['F4'].value + ", " + "кабинет: ") + str(sheet['F5'].value) + '\n')
else:
    yrok6A_2 = ""

# 3урок
if (yrok6A_3 > 1):
    yrok6A_3 = ("3 урок: " + str(sheet['F6'].value + ", " + "кабинет: ") + str(sheet['F7'].value) + '\n')
else:
    yrok6A_3 = ""

# 4урок
if (yrok6A_4 > 1):
    yrok6A_4 = ("4 урок: " + str(sheet['F8'].value + ", " + "кабинет: ") + str(sheet['F9'].value) + '\n')
else:
    yrok6A_4 = ""

# 5урок
if (yrok6A_5 > 1):
    yrok6A_5 = ("5 урок: " + str(sheet['F10'].value + ", " + "кабинет: ") + str(sheet['F11'].value) + '\n')
else:
    yrok6A_5 = ""
# 6урок
if (yrok6A_6 > 1):
    yrok6A_6 = ("6 урок: " + str(sheet['F12'].value + ", " + "кабинет: ") + str(sheet['F13'].value) + '\n')
else:
    yrok6A_6 = ""
# 7урок
if (yrok6A_7 > 1):
    yrok6A_7 = ("7 урок: " + str(sheet['F14'].value + ", " + "кабинет: ") + str(sheet['F15'].value) + '\n')
else:
    yrok6A_7 = ""
# все уроки

yrok6A = yrok6A_1 + yrok6A_2 + yrok6A_3 + yrok6A_4 + yrok6A_5 + yrok6A_6 + yrok6A_7
###################################################################################


#################################6B#################################################
yrok6B_1 = (len(str(sheet['G2'].value)))
yrok6B_2 = (len(str(sheet['G4'].value)))
yrok6B_3 = (len(str(sheet['G6'].value)))
yrok6B_4 = (len(str(sheet['G8'].value)))
yrok6B_5 = (len(str(sheet['G10'].value)))
yrok6B_6 = (len(str(sheet['G12'].value)))
yrok6B_7 = ((len(str(sheet['G14'].value))))

# 1урок
if (yrok6B_1 > 1):
    yrok6B_1 = ("1 урок: " + str(sheet['G2'].value + ", " + "кабинет: ") + str(sheet['F3'].value) + '\n')

# 2урок
if (yrok6B_2 > 1):
    yrok6B_2 = ("2 урок: " + str(sheet['G4'].value + ", " + "кабинет: ") + str(sheet['F5'].value) + '\n')

# 3урок
if (yrok6B_3 > 1):
    yrok6B_3 = ("3 урок: " + str(sheet['G6'].value + ", " + "кабинет: ") + str(sheet['G7'].value) + '\n')

# 4урок
if (yrok6B_4 > 1):
    yrok6B_4 = ("4 урок: " + str(sheet['G8'].value + ", " + "кабинет: ") + str(sheet['G9'].value) + '\n')
else:
    yrok6B_4 = ""
# 5урок
if (yrok6B_5 > 1):
    yrok6B_5 = ("5 урок: " + str(sheet['G10'].value + ", " + "кабинет: ") + str(sheet['G11'].value) + '\n')
else:
    yrok6B_5 = ""
# 6урок
if (yrok6B_6 > 1):
    yrok6B_6 = ("6 урок: " + str(sheet['G12'].value + ", " + "кабинет: ") + str(sheet['G13'].value) + '\n')
else:
    yrok6B_6 = ""
# 7урок
if (yrok6B_7 > 1):
    yrok6B_7 = ("7 урок: " + str(sheet['G14'].value + ", " + "кабинет: ") + str(sheet['G15'].value) + '\n')
else:
    yrok6B_7 = ""
# все уроки
yrok6B = yrok6B_1 + yrok6B_2 + yrok6B_3 + yrok6B_4 + yrok6B_5 + yrok6B_6 + yrok6B_7

###################################################################################


#################################6V#################################################
yrok6V_1 = (len(str(sheet['H2'].value)))
yrok6V_2 = (len(str(sheet['H4'].value)))
yrok6V_3 = (len(str(sheet['H6'].value)))
yrok6V_4 = (len(str(sheet['H8'].value)))
yrok6V_5 = (len(str(sheet['H10'].value)))
yrok6V_6 = (len(str(sheet['H12'].value)))
yrok6V_7 = ((len(str(sheet['H14'].value))))

# 1урок
if (yrok6V_1 > 1):
    yrok6V_1 = ("1 урок: " + str(sheet['H2'].value + ", " + "кабинет: ") + str(sheet['H3'].value) + '\n')

# 2урок
if (yrok6V_2 > 1):
    yrok6V_2 = ("2 урок: " + str(sheet['H4'].value + ", " + "кабинет: ") + str(sheet['H5'].value) + '\n')

# 3урок
if (yrok6V_3 > 1):
    yrok6V_3 = ("3 урок: " + str(sheet['H6'].value + ", " + "кабинет: ") + str(sheet['H7'].value) + '\n')

# 4урок
if (yrok6V_4 > 1):
    yrok6V_4 = ("4 урок: " + str(sheet['H8'].value + ", " + "кабинет: ") + str(sheet['H9'].value) + '\n')
else:
    yrok6V_4 = ""
# 5урок
if (yrok6V_5 > 1):
    yrok6V_5 = ("5 урок: " + str(sheet['H10'].value + ", " + "кабинет: ") + str(sheet['H11'].value) + '\n')
else:
    yrok6V_5 = ""
# 6урок
if (yrok6V_6 > 1):
    yrok6V_6 = ("6 урок: " + str(sheet['H12'].value + ", " + "кабинет: ") + str(sheet['H13'].value) + '\n')
else:
    yrok6V_6 = ""
# 7урок
if (yrok6V_7 > 1):
    yrok6V_7 = ("7 урок: " + str(sheet['H14'].value + ", " + "кабинет: ") + str(sheet['H15'].value) + '\n')
else:
    yrok6V_7 = ""
# все уроки
yrok6V = yrok6V_1 + yrok6V_2 + yrok6V_3 + yrok6V_4 + yrok6V_5 + yrok6V_6 + yrok6V_7

###################################################################################


#################################6G#################################################
yrok6G_1 = (len(str(sheet['I2'].value)))
yrok6G_2 = (len(str(sheet['I4'].value)))
yrok6G_3 = (len(str(sheet['I6'].value)))
yrok6G_4 = (len(str(sheet['I8'].value)))
yrok6G_5 = (len(str(sheet['I10'].value)))
yrok6G_6 = (len(str(sheet['I12'].value)))
yrok6G_7 = ((len(str(sheet['I14'].value))))

# 1урок
if (yrok6G_1 > 1):
    yrok6G_1 = ("1 урок: " + str(sheet['I2'].value + ", " + "кабинет: ") + str(sheet['I3'].value) + '\n')

# 2урок
if (yrok6G_2 > 1):
    yrok6G_2 = ("2 урок: " + str(sheet['I4'].value + ", " + "кабинет: ") + str(sheet['I5'].value) + '\n')

# 3урок
if (yrok6G_3 > 1):
    yrok6G_3 = ("3 урок: " + str(sheet['I6'].value + ", " + "кабинет: ") + str(sheet['I7'].value) + '\n')

# 4урок
if (yrok6G_4 > 1):
    yrok6G_4 = ("4 урок: " + str(sheet['I8'].value + ", " + "кабинет: ") + str(sheet['I9'].value) + '\n')
else:
    yrok6G_4 = ""
# 5урок
if (yrok6G_5 > 1):
    yrok6G_5 = ("5 урок: " + str(sheet['I10'].value + ", " + "кабинет: ") + str(sheet['I11'].value) + '\n')
else:
    yrok6G_5 = ""
# 6урок
if (yrok6G_6 > 1):
    yrok6G_6 = ("6 урок: " + str(sheet['I12'].value + ", " + "кабинет: ") + str(sheet['I13'].value) + '\n')
else:
    yrok6G_6 = ""
# 7урок
if (yrok6G_7 > 1):
    yrok6G_7 = ("7 урок: " + str(sheet['I14'].value + ", " + "кабинет: ") + str(sheet['I15'].value) + '\n')
else:
    yrok6G_7 = ""
# все уроки
yrok6G = yrok6G_1 + yrok6G_2 + yrok6V_3 + yrok6G_4 + yrok6G_5 + yrok6G_6 + yrok6G_7

###################################################################################


bot = telebot.TeleBot('1201504985:AAGMYqDdtcvzHVKwvEE-62Jh3v97yUGGp3w')


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/уроки 📖")

    markup.add(item1)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>,  могу сказать, какие у тебя сегодня уроки🧠.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['уроки'])
def yroki(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("5")
    item2 = types.KeyboardButton("6")
    item3 = types.KeyboardButton("7")
    item4 = types.KeyboardButton("8")
    item5 = types.KeyboardButton("9")
    item6 = types.KeyboardButton("10")
    item7 = types.KeyboardButton("11")

    markup.add(item1, item2, item3, item4, item5, item6, item7, )

    bot.send_message(message.chat.id,
                     "Чтобы я понял, какие у тебя уроки, выбери свой класс".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '5':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("5А", callback_data='5A')
            item2 = types.InlineKeyboardButton("5Б", callback_data='5B')
            item3 = types.InlineKeyboardButton("5В", callback_data='5V')
            item4 = types.InlineKeyboardButton("5Г", callback_data='5G')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)

        elif message.text == '6':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("6А", callback_data='6A')
            item2 = types.InlineKeyboardButton("6Б", callback_data='6B')
            item3 = types.InlineKeyboardButton("6В", callback_data='6V')
            item4 = types.InlineKeyboardButton("6Г", callback_data='6G')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)

        elif message.text == '7':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("7А", callback_data='7A')
            item2 = types.InlineKeyboardButton("7Б", callback_data='7B')
            item3 = types.InlineKeyboardButton("7В", callback_data='7V')
            item4 = types.InlineKeyboardButton("7Г", callback_data='7G')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)


        else:
            bot.send_message(message.chat.id, 'Я не понял тебя, чтобы узнать, что я умею, напиши /start')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '5A':
                bot.send_message(call.message.chat.id, yrok5A)
            elif call.data == '5B':
                bot.send_message(call.message.chat.id, yrok5B)
            elif call.data == '5V':
                bot.send_message(call.message.chat.id, yrok5V)
            elif call.data == '5G':
                bot.send_message(call.message.chat.id, yrok5G)

            elif call.data == '6A':
                bot.send_message(call.message.chat.id, yrok6A)

            elif call.data == '6B':
                bot.send_message(call.message.chat.id, yrok6B)

            elif call.data == '6V':
                bot.send_message(call.message.chat.id, yrok6V)

            elif call.data == '6G':
                bot.send_message(call.message.chat.id, yrok6G)

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Твои уроки на сегодня:",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Удачи в школе 💡 ")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
