
import requests

country = input("Введите страну, в которую вы собираетесь полететь: ")

if country == "Франция":
    print("Вы направляетесь в Париж!")
elif country == "Китай":
    print("Вы направляетесь в Пекин!")
elif country == "США":
    print("Вы направляетесь в Нью-йорк!")
else:
    print("К сожалению, мы не летаем в эту страну.")



def convert_currency(amount, from_currency, to_currency):
    api_url = 'https://v6.exchangerate-api.com/v6/9220b09c5d106ed75d957a2f/latest/USD' + from_currency

    response = requests.get(api_url)
    data = response.json()
    exchange_rate = data['rates'][to_currency]

    converted_amount = round(amount * exchange_rate, 2)


    return converted_amount
rubles = int(input())
euros = convert_currency(rubles, 'RUB', 'EUR')
yuan = convert_currency(rubles, 'RUB', 'CNY')
dollars = convert_currency(rubles, 'RUB', 'USD')

print(f'{rubles} RUB = {euros} EUR')
print(f'{rubles} RUB = {yuan} CNY')
print(f'{rubles} RUB = {dollars} USD')