
from datetime import datetime, timedelta
import redis
from flask import Flask
import requests

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379) # default port for Redis

def get_bitcoin_price():
	# defining key/request url
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    data = requests.get(url)
    data_json = data.json()
	# Convert the price to a floating point number
    return (data_json['price'])

def get_bitcoin_avg():
    prices = list()
    now = datetime.now()  
    now_plus_10 = now + timedelta(minutes = 0.1)

    while now < now_plus_10:
        price = get_bitcoin_price()
        now = datetime.now()  
        prices.append(price)

    sum = 0
    for i in prices:
        sum += float(i)
    
    avg = sum / len(prices)
    return avg

@app.route('/')
def hello():
    price = float((get_bitcoin_price()))
    avg = float((get_bitcoin_avg()))
    ans = "BitCoin price: " + str("{:.2f}".format(price)) + "  /  " + " BitCoin average: " + str("{:.2f}".format(avg))
    return (ans)
        


