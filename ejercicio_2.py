import requests # install requests with `pip install requests`

# 1 de Marzo de 2023 entre 12:00 y 13:00 GMT -3:00
# timestamp 12:00 GMT -3:00 1677682800000 in ms
# timestamp 13:00 GMT -3:00 1677686400000 in ms

# 1 de Marzo de 2024 entre 12:00 y 13:00 GMT -3:00
# timestamp 12:00 GMT -3:00 1709305200000 in ms
# timestamp 13:00 GMT -3:00 1709308800000 in ms

# EJERCICIO 2
# En comparación con el mismo día del año anterior, ¿cuál fue el aumento porcentual en el volumen de transacciones (en BTC)? (truncar en 2 decimales)

# 2024
entries = []
MAX_TIME_2024 = '1709308800000'
MIN_TIME_2024 = '1709305200000'

# get all entries
url = 'https://www.buda.com/api/v2/markets/BTC-CLP/trades?timestamp=' + MAX_TIME_2024 + '?limit=100'
response = requests.get(url).json()['trades']
entries += response['entries']
while(response['last_timestamp'] > MIN_TIME_2024):
  url = 'https://www.buda.com/api/v2/markets/BTC-CLP/trades?timestamp=' + response['last_timestamp'] + '?limit=100'
  response = requests.get(url).json()['trades']
  if(response['entries']):
    entries += response['entries']

# filter out entries with timestamp lower than MIN_TIME_2024
filtered_entries = [ entry for entry in entries if entry[0] >= MIN_TIME_2024 ]

# sum of all BTC transactions (remember to str -> float)
transaction_sum = 0
for entry in filtered_entries:
  transaction_sum += float(entry[1])

# truncate and print value
total_transactions_2024 = round(transaction_sum, 2)
print('VALUE FOR 2024:', round(transaction_sum, 2))

#2023
entries = []
MAX_TIME_2023 = '1677686400000'
MIN_TIME_2023 = '1677682800000'
# get all entries
url = 'https://www.buda.com/api/v2/markets/BTC-CLP/trades?timestamp=' + MAX_TIME_2023 + '?limit=100'
response = requests.get(url).json()['trades']
entries += response['entries']
while(response['last_timestamp'] > MIN_TIME_2023):
  url = 'https://www.buda.com/api/v2/markets/BTC-CLP/trades?timestamp=' + response['last_timestamp'] + '?limit=100'
  response = requests.get(url).json()['trades']
  if(response['entries']):
    entries += response['entries']

# filter out entries with timestamp lower than MIN_TIME_2023
filtered_entries = [ entry for entry in entries if entry[0] >= MIN_TIME_2023 ]

# sum of all BTC transactions (remember to str -> float)
transaction_sum = 0
for entry in filtered_entries:
  transaction_sum += float(entry[1])

total_transactions_2023 = round(transaction_sum, 2)
print('VALUE FOR 2023:', round(transaction_sum, 2))

# get %
print(round(((total_transactions_2024/total_transactions_2023) * 100) - 100, 2))
