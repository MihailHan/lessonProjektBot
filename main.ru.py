import requests
import pprint
import time
with open('token.txt') as f:
    token = f.read()

# #Оставляет только последние изменения(сообщения)
# endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
# params = {'timeout' : 60, 'offset': 0}
# response = requests.get(endPoint, params=params).json()['result']
# pprint.pprint(response)



#Бесконечные ответы
offset = -2
while True:
    endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
    params = {'timeout': 60, 'offset': offset +1}
    response = requests.get(endPoint, params=params).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        userText = response['result'][0]['message']['text']
        chatID = response['result'][0]['message']['chat']['id']
        endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chatID, 'text': userText}
        res = requests.get(endPoint, params=params)
    time.sleep(1)


# endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
# response = requests.get(endPoint).json()['result']
# pprint.pprint(response)
#
#
#
# usersInfo = dict()
# for i in response:
#     chatID = i['message']['chat']['id']
#     userName = i['message']['chat']['first_name']
#     if 'text' in i['message']:
#         userText = i['message']['text']
#     usersInfo[chatID] = [userName, userText]
#
#
# print(usersInfo)
#
# endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
# for user in usersInfo:
#     mes = f'Привет, {usersInfo[user][0]}!'
#     params = {'chat_id': user, 'text': mes}
# response = requests.get(endPoint, params=params)


