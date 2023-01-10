from fastapi import FastAPI, HTTPException
import requests

from helpers import allowed_stock

app = FastAPI()


@app.get('/')
def root():
  return {'message': 'Hello World'}

@app.get('/historical_data')
def historical_data(stock: str, start: str, end: str):
  if not allowed_stock(stock):
    raise HTTPException(status_code=404, detail='Stock not found')

  api_key = 'c13a5d2ecf7cc6b8c50c06d7e1dfce22'
  api_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{stock}?from={start}&to={end}&apikey={api_key}'
  response = requests.get(api_url)
  data = response.json()
  
  return data
