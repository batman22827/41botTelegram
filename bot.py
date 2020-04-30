# imports
import random
import datetime
import telebot
import xlrd, xlwt
import pyowm
import openpyxl
import string
import json
import traceback
import translit
from telebot import types
# config
with open("config.json", 'r') as f:
    config = json.load(f)

classCells = string.ascii_uppercase[1:-6]

bot = telebot.TeleBot(config['token'])
owm = pyowm.OWM(config['owmtoken'], language = "ru")





observation = owm.weather_at_place('Тюмень')
w = observation.get_weather()
t = w.get_temperature('celsius')["temp"]
t = int(t)
hums = w.get_humidity()




@bot.message_handler(commands=['lessons'])
def yroki(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/5🎓")
    item2 = types.KeyboardButton("/6📝")
    item3 = types.KeyboardButton("/7✏️")
    item4 = types.KeyboardButton("/8🔔")
    item5 = types.KeyboardButton("/9🖇")
    item6 = types.KeyboardButton("/10🎒")
    item7 = types.KeyboardButton("/11📚")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, "Чтобы я понял, какие у тебя уроки, выбери свой класс", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/lessons 📖")
    item2 = types.KeyboardButton("/temperature ")
    item3 = types.KeyboardButton("/help")

    markup.add(item1,item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>,  могу сказать, какие у тебя сегодня уроки🧠.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
@bot.message_handler(commands=['help'])
def help(message):
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/lessons 📖")
        item2 = types.KeyboardButton("/temp")
        item3 = types.KeyboardButton("/help")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id,
                         "Cписок доступных комманд:\n /start-начало работы с ботом\n /lessons-вывод списка уроков на текущий день\n/t-текущая температура и рекомендация, что надеть ".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)



@bot.message_handler(commands=['t'])
def temp(message):
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        bot.send_message(message.chat.id, "Текущая температура на улице: " + str(t)+"°")
        if t < 10:
            bot.send_message(message.chat.id, "Тебе стоит одеться тепло, на улице холодно")
        elif t < 14:
            bot.send_message(message.chat.id, "Сейчас не  очень холодно, но надень что-нибудь теплое")
        else:
            bot.send_message(message.chat.id, "Температура классная")

@bot.message_handler(commands=['lessonstom'])
def lessontommorow(message):
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Понедельник")
        item2 = types.KeyboardButton("Вторник")
        item3 = types.KeyboardButton("Среда")
        item4 = types.KeyboardButton("Четверг")
        item5 = types.KeyboardButton("Пятница")
        markup.add(item1,item2,item3,item4,item5)
        bot.send_message(message.chat.id,
                         "На какой день недели?".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)







@bot.message_handler(content_types=['text'])
def klass (message):
    if message.chat.type == 'private':
        if message.text == '/5🎓':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("5А", callback_data='5A')
            item2 = types.InlineKeyboardButton("5Б", callback_data='5B')
            item3 = types.InlineKeyboardButton("5В", callback_data='5V')
            item4 = types.InlineKeyboardButton("5Г", callback_data='5G')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)

        elif message.text == '/6📝':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("6А", callback_data='6A')
            item2 = types.InlineKeyboardButton("6Б", callback_data='6B')
            item3 = types.InlineKeyboardButton("6В", callback_data='6V')
            item4 = types.InlineKeyboardButton("6Г", callback_data='6G')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)

        elif message.text == '/7✏️':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("7А", callback_data='7A')
            item2 = types.InlineKeyboardButton("7Б", callback_data='7B')
            item3 = types.InlineKeyboardButton("7В", callback_data='7V')
            item4 = types.InlineKeyboardButton("7Г", callback_data='7G')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)

        elif message.text == '/8🔔':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("8А", callback_data='8A')
            item2 = types.InlineKeyboardButton("8Б", callback_data='8B')
            item3 = types.InlineKeyboardButton("8В", callback_data='8V')


            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)


        elif message.text == '9🖇':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("9А", callback_data='9A')
            item2 = types.InlineKeyboardButton("9Б", callback_data='9B')
            item3 = types.InlineKeyboardButton("9В", callback_data='9V')
            item4 = types.InlineKeyboardButton("9Г", callback_data='9G')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)

        elif message.text == '/10':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("10Асоц-гум", callback_data='10S')
            item2 = types.InlineKeyboardButton("10физ-мат", callback_data='10F')
            item3 = types.InlineKeyboardButton("10В", callback_data='10B')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Теперь выбери букву класса', reply_markup=markup)


        else:
            bot.send_message(message.chat.id, 'Я не понял тебя, чтобы узнать, что я умею, напиши /help')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            db = DataBase(config['days']['понедельник'])
            s = ""
            for i, k  in enumerate(db.sheet[call.data].keys()): 
                s += f"{i+1} урок: {k}, кабинет: {db.sheet[call.data][k]}\n"
            bot.send_message(call.message.chat.id, s)

    except:
        traceback.print_exc()

class DataBase ( object ):
    def __scrapClasees(self): 
        for cell in classCells:
            className = self.activeSheet[cell + "1"].value
            className = translit.transliterate(className).upper()
            self.sheet[className] = {}
            for i in range(2, 15, 2):
                lesson = self.activeSheet[f"{cell}{i}"].value
                room = self.activeSheet[f"{cell}{i+1}"].value
                if (lesson != '\xa0'):
                    self.sheet[className][lesson] = room
    def __init__(self, dbname):
        self.database = openpyxl.load_workbook(dbname)
        self.sheetNames = self.database.sheetnames
        self.activeSheet = self.database.active
        self.sheet = {}
        self.__scrapClasees()

bot.polling(none_stop=True)
