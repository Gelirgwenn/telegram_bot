import requests
import time


API_URL = 'https://api.telegram.org/bot'
# API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'  # кошки не работают
# CATS_TOKEN = 'live_mu8FMqBx803Acd5Q0ljlRnsxEM8ecIMOGL4FbArDy9vGdI6wKJ8PEVbtu7MNNYEM'
API_CATS_URL = 'https://randomfox.ca/floof/'  # Лисички
BOT_TOKEN = '6609249256:AAHHjwi7Kw-T-Wdr54EdcJLURAObfUKk4y4'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
cat_response: requests.Response
cat_Link: str

while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()


    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
        #    print(cat_response.text)
            if cat_response.status_code == 200:
            #    cat_link = cat_response.json()[0]['url'] # кошки
                cat_link = cat_response.json()['image']  # Лиса
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1





    # if updates['result']:
    #     for result in updates['result']:
    #         offset = result['update_id']
    #         chat_id = result['message']['from']['id']
    #         cat_response = requests.get(API_CATS_URL)
    #         print(cat_response)
    #
    #         for i in cat_response:
    #             print(i['url'])
    #      #   cat_response = requests.get(f'{API_CATS_URL}{CATS_TOKEN}')
    #             print(cat_response.text)
    #             if cat_response.status_code == 200:
    #                 cat_link = cat_response.json()[0]['url'] # кошки
    #           #  cat_link = cat_response.json()['image']  # Лиса
    #                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
    #             else:
    #                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    #
    # time.sleep(1)
    # counter += 1





















    # if updates['result']:
    #     for result in updates['result']:
    #         offset = result['update_id']
    #         chat_id = result['message']['from']['id']
    #         cat_response = requests.get(API_CATS_URL)
    #      #   for i in cat_response:
    #      #   cat_response = requests.get(f'{API_CATS_URL}{CATS_TOKEN}')
    #         print(cat_response.text)
    #         if cat_response.status_code == 200:
    #             cat_link = cat_response.json()[0]['url'] # кошки
    #           #  cat_link = cat_response.json()['image']  # Лиса
    #             requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
    #         else:
    #             requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    #
    # time.sleep(1)
    # counter += 1




# while counter < 100:
#     print('attempt = ', counter)
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         print(updates)
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(API_CATS_URL)
#             if cat_response.status_code == 200:
#                 print('qweqqqqqqqqqqqqqq')
#                 cat_Link = cat_response.json()[0]['url']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_Link}')
#             else:
#                 print('3333333333333333333333333')
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
#     time.sleep(1)
#     counter +=1