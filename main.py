import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6609249256:AAHHjwi7Kw-T-Wdr54EdcJLURAObfUKk4y4'
TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

# https://api.telegram.org/bot6609249256:AAHHjwi7Kw-T-Wdr54EdcJLURAObfUKk4y4/getUpdates

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    print(updates)

    if updates['result']:

        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1




#requests.get(f'{'https://api.telegram.org/bot'}{'6609249256:AAHHjwi7Kw-T-Wdr54EdcJLURAObfUKk4y4'}/sendMessage?chat_id={949125930}&text={"AMAZING!"}')



# https://api.telegram.org/bot6609249256:AAHHjwi7Kw-T-Wdr54EdcJLURAObfUKk4y4/sendMessage?chat_id=949125930&text="AMAZING!"



# https://api.telegram.org/bot<token>/sendMessage?chat_id - <chat_id>&text=AMAZING!









# import requests
#
#
# def mult(a, b):
#     return a * b
#
#
# def min(a, b):
#     return a - b
#
#
# def get_tuple(lst: list[float | bool]) -> tuple[int]:
#     # return tuple(int(num) for num in lst)
#     return tuple(map(int, lst))
#
#
# if __name__ == '__main__':
#     print(get_tuple([0.23, 3.12, True, 5.22]))
#     print(mult(2, 5))
#     print(min(9, 3))
#     print('как то так')
#     # n = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/btc.json')
#     # print(n.json())
#     #  api_url = 'http://api.open-notify.org/iss-now.json'
#     api_url = 'http://numbersapi.com/43'
#
#     response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response
#
#     if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
#         print(response.text)
#     #     print(response.text.split()[1])
#     else:
#         print(response.status_code)  # При другом коде ответа выводим этот код
