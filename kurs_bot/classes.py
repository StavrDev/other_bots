import sqlite3
import requests
import lxml
from bs4 import BeautifulSoup as BS
from aiogram import types

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (user_id INTEGER PRIMARY KEY)''')
        self.conn.commit()

    def add_user(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        if not self.cursor.fetchone():
            self.cursor.execute('INSERT INTO users VALUES (?)', (user_id,))
            self.conn.commit()
            print(f"User {user_id} added successfully.")
        else:
            print(f"User {user_id} already exists.")

    def get_total_records(self):
        query = "SELECT COUNT(*) FROM users;"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    
    def close(self):
        self.conn.close()

class Parser:
    def __init__(self):
        self.result = ""

    def parse_crypto(self):
        url_btc = "https://www.binance.com/ru/price/bitcoin"
        responce = requests.get(url_btc)
        result_btc = BS(responce.text, 'lxml')
        btc_find = result_btc.find("div", "css-zo19gu")
        btc = BS(btc_find.text, 'lxml').text.strip()

        url_eth = "https://www.binance.com/ru/price/ethereum"
        responce = requests.get(url_eth)
        result_eth = BS(responce.text, 'lxml')
        eth_find = result_eth.find("div", "css-zo19gu")
        eth = BS(eth_find.text, 'lxml').text.strip()

        url_zcash = "https://www.binance.com/ru/price/zcash"
        responce = requests.get(url_zcash)
        result_zcash = BS(responce.text, 'lxml')
        zcash_find = result_zcash.find("div", "css-zo19gu")
        zcash = BS(zcash_find.text, 'lxml').text.strip()
        self.result = "1 Bitcoin = {}\n1 Ethereum = {}\n1 Zcash = {}".format(btc, eth, zcash)

    def parse_currency(self):
        url_usd = "https://www.banki.ru/products/currency/usd/"
        responce = requests.get(url_usd)
        result_usd = BS(responce.text, 'lxml')
        usd_find = result_usd.find('div', "Text__sc-j452t5-0 oCMVU")
        usd = BS(usd_find.text, 'lxml').text.strip()

        url_euro = "https://www.banki.ru/products/currency/eur/"
        responce = requests.get(url_euro)
        result_euro = BS(responce.text, 'lxml')
        euro_find = result_euro.find('div', class_="Text__sc-j452t5-0 oCMVU")
        euro = BS(euro_find.text, 'lxml').text.strip()
        self.result = "1 Доллар = {}\n1 Евро = {}".format(usd, euro)

    def get_result_currency(self):
        return self.result

    def get_result_crypto(self):
        return self.result

