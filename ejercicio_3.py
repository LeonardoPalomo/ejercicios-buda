import requests # install requests with `pip install requests`

# 1 de Marzo de 2024 entre 12:00 y 13:00 GMT -3:00
# timestamp 12:00 GMT -3:00 1709305200000 in ms
# timestamp 13:00 GMT -3:00 1709308800000 in ms

# EJERCICIO 3
# Considerando que la comisión normal corresponde a un 0.8% ¿Cuánto dinero (en CLP) se dejó de ganar debido 
# a la liberación de comisiones durante el BlackBuda? (truncar en 2 decimales)
entries = []
MAX_TIME = '1709308800000'
MIN_TIME = '1709305200000'

# get all entries
url = 'https://www.buda.com/api/v2/markets/BTC-CLP/trades?timestamp=' + MAX_TIME + '?limit=100'
response = requests.get(url).json()['trades']
entries += response['entries']
while(response['last_timestamp'] > MIN_TIME):
  url = 'https://www.buda.com/api/v2/markets/BTC-CLP/trades?timestamp=' + response['last_timestamp'] + '?limit=100'
  response = requests.get(url).json()['trades']
  if(response['entries']):
    entries += response['entries']

# filter out entries with timestamp lower than MIN_TIME (1709305200000)
filtered_entries = [ entry for entry in entries if entry[0] >= MIN_TIME ]

# sum of all CLP transactions (remember to str -> float)
commision_sum = 0
for entry in filtered_entries:
  commision_sum += float(entry[2]) * 0.008

# truncate and print value
print(round(commision_sum, 2))

# de manera alternativa, se puede sacar el 0.8% del resultado del ejercicio 1