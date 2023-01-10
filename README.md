# Prueba de Backend - Trii

Para la realización de la prueba se decidió desarrollar la primera opción (manejo histórico de datos)

## Primer punto

Para la creación del endpoint pedido se construyó una api con fastapi. Para ejecutar la app se deben seguir los siguientes pasos:

1. Instalar requerimientos: ```pip install -r requirements.txt```
2. Correr la aplicación: ```uvicorn main:app --reload --host 0.0.0.0 --port 8000```

El endpoint  ```GET /historical_data```, el cual se encuentra en la branch ```main``` está encargado de consultar a una api los precios diarios históricos de una acción entre las fechas entregadas. El endpoint acepta los parámetros:

* ```stock```: nombre de la acción de la cual se quiere obtener la información
* ```start```: fecha desde la cual se quiere obtener la información. Tiene que ser entregada en el formato YYYY-MM-DD
* ```end```: fecha hasta la cual se quiere obtener la información. Tiene que ser entregada en el formato YYYY-MM-DD

Un ejemplo de una request que se puede realizar en postman es:
`http://localhost:8000/historical_data?stock=AAPL&start=2022-12-28&end=2022-12-31`

## Segundo punto

El script stocks_info.py, el cual se encuentra en la branch ```cli-script``` está encargado de obtener la información de todas las acciones listadas y sus respectivas empresas. Para correr el script se debe ejecutar lo siguiente:

```python3 stocks_info.py```