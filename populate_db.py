import os
import sqlite3
import alpaca_trade_api as tradeapi

from dotenv import load_dotenv
load_dotenv()

ID = os.getenv('ID')
SECRET_KEY = os.getenv('SECRET_KEY')
BASE_URL = os.getenv('BASE_URL')

connection = sqlite3.connect('app.db')
cursor = connection.cursor()

api = tradeapi.REST(ID, SECRET_KEY, BASE_URL)
assets = api.list_assets()

for asset in assets:
    print(asset.name)

for asset in assets:
    try:
        if asset.status == 'active':
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)




connection.commit()