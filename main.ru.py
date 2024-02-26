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


#Функция, дает косм.фото по дате
def givePhoto(date: str) -> (str,str):
    endPoint = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': 'DEMO_KEY', 'date': date}
    res = requests.get(endPoint, params=params).json()
    explanation = res['explanation']
    urlPhoto = res['url']
    return (urlPhoto,explanation)


#Заготовка для бота с функцией
# endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
# res = requests.get(endPoint).json()
# chatID = res['result'][0]['message']['chat']['id']
# endPoint = f'https://api.telegram.org/bot{token}/sendPhoto'
# params = {'chat_id':chatID, 'photo':givePhoto('2024-01-24')[0]}
# response = requests.get(endPoint, params=params).json()



#Бесконечные ответы (в последствии эхо - бот)
offset = -2
while True:
    endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
    params = {'timeout': 60, 'offset': offset +1}
    response = requests.get(endPoint, params=params).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        chatID = response['result'][0]['message']['chat']['id']
        userText = response['result'][0]['message']['text']
        photoURL, photoEXP = givePhoto(userText)
        endPoint = f'https://api.telegram.org/bot{token}/sendPhoto'
        params = {'chat_id':chatID, 'photo':photoURL}
        response = requests.get(endPoint, params=params)
        endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chatID, 'text':photoEXP}
        response = requests.get(endPoint, params=params)
    time.sleep(1)




#Отправка еденичного сообщения (не автомат)
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


























