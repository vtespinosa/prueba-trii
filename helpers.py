from tkinter import ALL


ALLOWED_STOCKS = [
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

def allowed_stock(stock: str):
  return stock in ALLOWED_STOCKS