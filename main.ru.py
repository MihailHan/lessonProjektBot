import requests
import pprint
with open('token.txt') as f:
    token = f.read()

import time
while True:



endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(endPoint).json()['result']
pprint.pprint(response)


mes = f'Привет, {response[0]['message']['from']['first_name']}!'
chatID = response[0]['message']['chat']['id']
usersInfo = dict()
for i in response:
    chatID = i['message']['chat']['id']
    userName = i['message']['chat']['first_name']
    if 'text' in i['message']:
        userText = i['message']['text']
    usersInfo[chatID] = [userName, userText]


print(usersInfo)

endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
params = {'chat_id': chatID, 'text': mes}
response = requests.get(endPoint, params=params)
for user in usersInfo:
    mes = f'Привет, {usersInfo[user][0]}!'
    params = {'chat_id': user, 'text': mes}
    res = requests.get(endPoint, params=params)



