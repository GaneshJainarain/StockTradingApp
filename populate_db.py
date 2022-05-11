import os
import sqlite3
import alpaca_trade_api as tradeapi
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv('ID')
SECRET_KEY = os.getenv('SECRET_KEY')
BASE_URL = os.getenv('BASE_URL')

connection = sqlite3.connect('/Users/richeyjay/Desktop/StockTradingApp/app.db')
#Whenever we query this returns a Sqlite3 object
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

""" Getting the records that are already in our DB """
 
cursor.execute("""
    SELECT symbol, company FROM stock
""")

""" Putting all of the alreaddy existing companies in a list """
""" To see which stocks arent already in the list and got updated since last population"""
rows = cursor.fetchall()

#Building our list of stocks in our DB, list comprehension
symbols = [row['symbol'] for row in rows]

api = tradeapi.REST(ID, SECRET_KEY, BASE_URL)
assets = api.list_assets()

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)

connection.commit()
