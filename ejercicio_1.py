import requests # install requests with `pip install requests`

# 1 de Marzo de 2024 entre 12:00 y 13:00 GMT -3:00
# timestamp 12:00 GMT -3:00 1709305200000 in ms
# timestamp 13:00 GMT -3:00 1709308800000 in ms

# EJERCICIO 1
# ¿Cuánto dinero (en CLP) se transó durante el evento "Black Buda" BTC-CLP ? (truncar en 2 decimales)
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
transaction_sum = 0
for entry in filtered_entries:
  transaction_sum += float(entry[2])

# truncate and print value
print(round(transaction_sum, 2))
