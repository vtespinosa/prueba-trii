import requests
import json
import os

STOCKS = [
  'AAPL',
  'GOOGL',
  'AMZN',
  'TSLA',
  'FB',
  'TWTR',
  'UBER',
  'LYFT',
  'SNAP',
  'SHOP'
]

#Create data directory
if not os.path.exists('data'):
  os.makedirs('data')

# Request stocks information
api_key = 'c13a5d2ecf7cc6b8c50c06d7e1dfce22'
stocks_text = ','.join(STOCKS)
api_url = f'https://financialmodelingprep.com/api/v3/quote/{stocks_text}?apikey={api_key}'
response = requests.get(api_url)
data = response.json()

# Save stocks data in json files
for stock in data:
  symbol = stock['symbol']
  with open(f'data/{symbol}.json', 'w') as f:
    json.dump(data, f)
