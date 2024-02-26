import requests
import pprint
with open('token.txt') as f:
    token = f.read()

# import time
# while True:
#     #получить информацию по всем событиям (апдейтам)
#     endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
#     response = requests.get(endPoint).json()['result']
#     userText = response[0]['message']['text']
#     chatID = response[0]['message']['chat']['id']
#     #pprint.pprint(response)
#     endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
#     params = {'chat_id': chatID, 'text': userText}
#     res = requests.get(endPoint, params=params)
#     time.sleep(1)


endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(endPoint).json()['result']
pprint.pprint(response)



usersInfo = dict()
for i in response:
    chatID = i['message']['chat']['id']
    userName = i['message']['chat']['first_name']
    if 'text' in i['message']:
        userText = i['message']['text']
    usersInfo[chatID] = [userName, userText]


print(usersInfo)

endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
for user in usersInfo:
    mes = f'Привет, {usersInfo[user][0]}!'
    params = {'chat_id': user, 'text': mes}
response = requests.get(endPoint, params=params)


