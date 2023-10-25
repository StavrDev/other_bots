import lxml
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

commands = """
/help - помощь
/value - значение всех датчиков
/start - перезапуск бота
/report - сообщить об ошибке
"""

def analytics(func: callable):
    total_messages = 0
    users = set()
    total_users = 0
    def analytics_wrapper(message):
        nonlocal total_messages, total_users
        total_messages += 1
        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users += 1
        print("Новое сообщение:", message.text, 'Всего сообщений:', total_messages, 'Всего пользователей:', total_users)
        return func(message)
    return analytics_wrapper

#parsing
def vareg(message): 
    headers = {
        'Origin': 'https://narodmon.ru',
        'Referer': 'https://narodmon.ru/9978'
    }
    
    r = requests.post('https://narodmon.ru/devmap/9978', data={'ajax': 1}, headers=headers)
    
    soup = BeautifulSoup(r.text, 'lxml')
    temp = float(soup.find('b').text[:-1])
    bot.send_message(message.chat.id,"Температура в Вартемягах сейчас " + str(temp) + '°C')

def alag(message):
    headers = {
        'Origin': 'https://narodmon.ru',
        'Referer': 'https://narodmon.ru/9880'
    }
    
    r = requests.post('https://narodmon.ru/devmap/9880', data={'ajax': 1}, headers=headers)
    
    soup = BeautifulSoup(r.text, 'lxml')
    temp = float(soup.find('b').text[:-1])
    bot.send_message(message.chat.id,"Температура в Агалатово сейчас " + str(temp) + '°C')

def sel(message):
    headers = {
        'Origin': 'https://narodmon.ru',
        'Referer': 'https://narodmon.ru/10182'
    }
    
    r = requests.post('https://narodmon.ru/devmap/10182', data={'ajax': 1}, headers=headers)
    
    soup = BeautifulSoup(r.text, 'lxml')
    temp = float(soup.find('b').text[:-1])
    bot.send_message(message.chat.id, "Температура в Селах сейчас " + str(temp) + '°C')

def bril(message):
    headers = {
        'Origin': 'https://narodmon.ru',
        'Referer': 'https://narodmon.ru/10114'
    }
    
    r = requests.post('https://narodmon.ru/devmap/10114', data={'ajax': 1}, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    temp = float(soup.find('b').text[:-1])
    bot.send_message(message.chat.id,"Температура в Бриллианте сейчас " + str(temp) + '°C')


bot = telebot.TeleBot("5658170708:AAEOnvLYZS_4_hWilxHRsufuHMH_L1-wAl4")
#bot

@bot.message_handler(commands=['start'])
@analytics
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 =  types.KeyboardButton('Выбрать датчик🔺')
    btn2 = types.KeyboardButton("Помощь🆘")
    btn3 = types.KeyboardButton("Общие показания🔻")
    btn4 = types.KeyboardButton("Сообщить об ошибке🛠")
    keyboard.add(btn1,btn2, btn3,btn4)
    bot.send_message(message.chat.id ,'Добро пожаловать в нашего бота!👋', reply_markup=keyboard)
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['help'])
@analytics
def help(message):
    bot.send_message(message.chat.id, commands)
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['report'])
@analytics
def report (message):
    bot.send_message(message.chat.id, 'Для того что бы сообщить об ошибке отпишите сюда: \nt.me/helpers_monitor')

@bot.message_handler(commands=['value'])
@analytics
def values(message):
    vareg(message)
    alag(message)
    sel(message)
    bril(message)

@bot.message_handler(content_types=['text'])
@analytics
def select(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True ,row_width=2)
    btn5 = types.KeyboardButton('Варемяги')
    btn6 = types.KeyboardButton('Агалатово')
    btn7 = types.KeyboardButton('Села')
    btn8 = types.KeyboardButton('Бриллиант')
    btn9 = types.KeyboardButton("Главное меню🏠")
    keyboard.add(btn5, btn6, btn7, btn8, btn9)
    if message.text == "Выбрать датчик🔺":
        bot.send_message(message.chat.id, 'Выберите местоположение датчика:', reply_markup=keyboard)
    if message.text == 'Варемяги':
        vareg(message)
    if message.text == 'Агалатово':
        alag(message)
    if message.text == 'Села':
        sel(message)
    if message.text == 'Бриллиант':
        bril(message)
    if message.text == 'Главное меню🏠':
        start(message)    

    if message.text == 'Общие показания🔻':
        vareg(message)
        alag(message)
        sel(message)
        bril(message)
    
    if message.text == "Помощь🆘":
        help(message)
        
    if message.text == 'Сообщить об ошибке🛠':
        report(message)
        bot.delete_message(message.chat.id, message.message_id)

bot.polling(none_stop=True)