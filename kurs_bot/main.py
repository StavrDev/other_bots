import logging  
import sqlite3
import tracemalloc
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from classes import Database, Parser
import markups as KB

admin_id = [1765180561]
tracemalloc.start()

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6226233593:AAH_IDCbjKHW4tvbhZK5EDvuI5Rf2qj_O3Q')
dp = Dispatcher(bot)
db = Database('data.db') 
db.create_table()

parser = Parser()



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет!\nЗдесь ты можешь узнать актуальный курс валют/криптовалют.\n\nВНИМАНИЕ!!! Загрузка курса может занять около 1-2х секунд\n\nВыберите действие ниже:", reply_markup=KB.keyboard)
    user_id = message.from_user.id
    db.add_user(user_id=user_id)
    

@dp.message_handler(commands='crypto')
async def crypto(message: types.Message):
    parser.parse_crypto()
    result_crypto = parser.get_result_crypto()
    await message.answer("Актуальный курс криптовалют:\n\n"+ result_crypto +"\n\nДанные взяты с binance.com", reply_markup=KB.kb_crypto)

@dp.message_handler(commands='currency')
async def crypto(message: types.Message):
    parser.parse_currency()
    result_currency = parser.get_result_currency()
    await message.answer("Актуальный курс Доллара/Евро:\n\n"+ result_currency, reply_markup=KB.kb_cur)

@dp.callback_query_handler(lambda callback_query: True)
async def handle_inline_button(callback_query: types.CallbackQuery):
    button_data = callback_query.data
    
    if button_data == 'crypto':
        parser.parse_crypto()
        result_crypto = parser.get_result_crypto()
        await bot.send_message(callback_query.from_user.id, "Актуальный курс криптовалют:\n\n"+ result_crypto +"\n\nДанные взяты с binance.com",reply_markup=KB.kb_crypto)
        
    elif button_data == "currency":
        parser.parse_currency()
        result_currency = parser.get_result_currency()
        await bot.send_message(callback_query.from_user.id,"Актуальный курс Доллара/Евро:\n\n"+ result_currency + "\n\nДанные взяты с banki.ru",reply_markup=KB.kb_cur)
    
    elif button_data == "back":
        await bot.send_message(callback_query.from_user.id,"Привет!\nЗдесь ты можешь узнать актуальный курс валют/криптовалют.\n\nВНИМАНИЕ!!! Загрузка курса может занять около 1-2х секунд\n\nВыберите действие ниже:", reply_markup=KB.keyboard)
    
    elif button_data == "update_crypto":
        parser.parse_crypto()
        result_crypto = parser.get_result_crypto()
        await bot.send_message(callback_query.from_user.id,"Актуальный курс Доллара/Евро:\n\n"+ result_crypto, reply_markup=KB.kb_crypto)

    elif button_data == "update_cur":
        parser.parse_currency()
        result_currency = parser.get_result_currency()
        await bot.send_message(callback_query.from_user.id,"Актуальный курс Доллара/Евро:\n\n"+ result_currency + "\n\nДанные взяты с banki.ru",reply_markup=KB.kb_cur)
        
    else:
        bot.answer_callback_query(callback_query.id, text="Ошибка:(")


"""РАССЫЛКА + СТАТИСТИКА"""
conn = sqlite3.connect('data.db')
cursor = conn.cursor()


async def send_message_to_all_users(message: str):
    query = "SELECT user_id FROM users"
    cursor.execute(query)
    results = cursor.fetchall()
    
    for result in results:
        user_id = result[0]
        await bot.send_message(user_id, message)
        await asyncio.sleep(0.05)

@dp.message_handler(commands=['send_all'])
async def send_all_users(message: types.Message):
    if message.from_user.id ==1765180561:
        text = message.text.split('/send_all ')[1]
        await send_message_to_all_users(text)
        await message.answer('Сообщение отправлено всем пользователям')
    else:
        await message.answer('У вас нет прав для выполнения этой команды')

@dp.message_handler(commands=['stats'])
async def stats(message: types.Message):    
    total_records = db.get_total_records()
    await message.answer("Общее количество пользователей: "+ str(total_records))
    

if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)