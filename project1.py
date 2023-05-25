import requests
print("Добро пожаловать! Куда бы Вы хотели поехать?")
print("1. США")
print("2. Китай")
print("3. Франция")

choice = input("Выберите один из вариантов (1/2/3): ")

if choice == '1':
    print("Приятного путешествия в США.Стоимость билета из Иркутска составляет 62 124 ")
elif choice == '2': 
    print("Китай ! Удачной поездки.Стоимость билета из Иркутска составляет 32 760")
elif choice == '3':
    print("Франция! Наслаждайтесь своей поездкой.Стоимость билета из Иркутска составляет 29 213")
else:
    print("Вы ввели неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

api_key = 'bf8dbb8030bd65be99d2aa75'
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/RUB'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

   
currencies = ['USD', 'EUR', 'CNY']


for currency in currencies:
    rate = data['conversion_rates'][currency]
    print(f'1 RUB = {rate} {currency}')

 
rubles = float(input('Введите количество рублей для конвертации: '))


print('Выберите валюту, на которую нужно конвертировать рубли:')
for i, currency in enumerate(currencies):
    print(f'{i + 1}. {currency}')

choice = int(input('Введите номер от 1 до 3: '))
currency = currencies[choice - 1]


converted = rubles / data['conversion_rates']['RUB'] * data['conversion_rates'][currency]

print(f'{rubles} RUB = {converted:.2f} {currency}')
