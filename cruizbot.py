import telebot

from telebot import types

bot = telebot.TeleBot("5889325246:AAFZIHm849FZ1RJ73PJP8QwXfdfJEHPsPgc")
 
@bot.message_handler(commands=['start'])
def welcome(message):
    
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Старт/В начало")
    

    
    markup.add(item1)

 
    
 
    bot.send_message(message.chat.id, "Добро пожаловать! Вас приветствует помощник подбора комплектующих для круиз контроля! У меня будет для вас несколько вопросов. ".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item3 = types.InlineKeyboardButton("2007-2009", callback_data='good')
        item4 = types.InlineKeyboardButton("2009-2013", callback_data='bad') 
        markup.add(item3, item4)
        if message.text == 'Старт/В начало':

            bot.send_message(message.chat.id, "Какой год выпуска вашего автомобиля?",reply_markup = markup)
           
 
            #bot.send_message(message.chat.id, '', )
        else:
            bot.send_message(message.chat.id, 'Ошибка!(')
 




@bot.callback_query_handler(func=lambda call: True)
def message(call):
    try:
        if call.message:
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton("1.4", callback_data = "meh", )
                item6 = types.InlineKeyboardButton("1.6", callback_data='var') 
                markup.add(item5, item6)
                if call.data == 'good':
                    bot.send_message(call.message.chat.id, 'Какой объем двигателя?',reply_markup = markup)
                
                markup = types.InlineKeyboardMarkup(row_width=2)
                item9 = types.InlineKeyboardButton("Да",callback_data = "da")
                item10 = types.InlineKeyboardButton("Нет", callback_data = "net")
                markup.add(item9, item10)
                if call.data == "bad":
                
                    bot.send_message(call.message.chat.id, "На вашем автомобиле уже установлены кнопки управления магнитолой?", reply_markup = markup)
               

    except Exception as e:
        print(repr(e))
    
    try:
        if call.message:    

            if call.data =="da":
                bot.send_message(call.message.chat.id , "Для установки круиз-контроля на Ваш автомобиль понадобятся:\n\nРычаг круиз контроля с проводом, винтами и заглушкой (Option 4): \nhttps://alii.pub/6krht7")
            elif call.data == "net":
                

                bot.send_message(call.message.chat.id , "Для установки круиз-контроля на Ваш автомобиль понадобятся:\n\nСпиральный провод: https://alii.pub/6krhyg\n\nРычаг круиз-контроля с проводом, винтами и заглушкой (Option 4): https://alii.pub/6krht7\n\nP.S. ВНИМАНИЕ! Есть вероятность того, что на вашем автомобиле не хватает некоторой части проводки! Пожалуйста,снимите кожух рулевой колонки и посмотрите проводку на спиральном проводе рядом с замком зажигания. Если у Вас присутствуют голубой и зеленый провод, то все в порядке! Если эти провода отсутствуют, то Вам придётся проложить дополнительный провод! Подробнее смотрите по ссылке: \nhttps://www.drive2.ru/l/503346803542851709")
                
                

               

    except Exception as e:
        print(repr(e))

    try:
        if call.message:

            if call.data == "meh":
                bot.send_message(call.message.chat.id , "На ваш автомобиль установлен дроссель с приводом на тросике, поэтому установить круиз контроль нельзя. Но вы можете установить кнопки на руль. Для этого вам необходимо приобрести:\n\nКнопки на руль: https://alii.pub/6ktecw\n\nСпиральный провод: https://alii.pub/6krhyg")

    except Exception as e:
        print(repr(e))
    try:
        if call.message:
            markup = types.InlineKeyboardMarkup(row_width=2)
            item7 = types.InlineKeyboardButton("Механика", callback_data = "mehan")
            item8 = types.InlineKeyboardButton("Робот", callback_data='robot') 
            markup.add(item7, item8)
            if call.data == "var":

                bot.send_message(call.message.chat.id ,"Какой тип КПП у Вас на автомобиле?", reply_markup= markup )

            
    except Exception as e:
        print(repr(e))
    try: 
        if call.message:
            if call.data == "mehan":
                bot.send_message(call.message.chat.id, "Для установки круиз-контроля на Ваш автомобиль понадобятся:\n\nСпиральный привод: https://alii.pub/6krhyg\n\nРычаг круиз-контроля с проводом и винтами (Option 1): https://alii.pub/6krht7\n\nЗаглушка (45186 - 02080-C0): https://alii.pub/6ktf2d\n\nТак же при желании Вы можете установить кнопки на руль (замена спирального провода обязательна!): https://alii.pub/6ktecw")
            elif call.data == 'robot':
                bot.send_message(call.message.chat.id, "Для установки круиз-контроля на Ваш автомобиль понадобятся:\n\nРычаг круиз-контроля с проводом и винтами (Option 1): https://alii.pub/6krht7\n\nЗаглушка (45186 - 02080-C0): https://alii.pub/6ktf2d\n\nТак же при желании Вы можете установить кнопки на руль (спиральный провод менять не требуется!): https://alii.pub/6ktecw")
        
            
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
