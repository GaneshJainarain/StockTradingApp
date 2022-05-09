import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
load_dotenv()

ID = os.getenv('ID')
SECRET_KEY = os.getenv('SECRET_KEY')
BASE_URL = os.getenv('BASE_URL')

api = tradeapi.REST(ID, SECRET_KEY, BASE_URL)
aapl = api.bars(['AAPL', 'day'])
print(aapl)