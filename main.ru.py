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

#Функция для проверки даты
def checkDate(userData: str) -> bool:
    if len(userData) != 10:
        return False
    lst = userData.split('-')
    if len(lst) != 3:
        return False
    if not all([len(lst[0]) == 4, len(lst[1]) == 2, len(lst[2]) == 2]):
        return False
    for item  in lst:
        if not all(map(lambda x: x.isdigit(), item)):
            return False
    year, month, day = int(lst[0]), int(lst[1]), int(lst[2])
    if not all([2000 <= year <= 2024, 1 <= month <= 12, 1 <= day <= 31]):
        return False
    return True

#Бот с астрономическими фото
offset = -2
while True:
    endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
    params = {'timeout': 60, 'offset': offset +1}
    response = requests.get(endPoint, params=params).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        chatID = response['result'][0]['message']['chat']['id']
        userText = response['result'][0]['message']['text']
        if checkDate(userText):
            photoURL, photoEXP = givePhoto(userText)
            endPoint = f'https://api.telegram.org/bot{token}/sendPhoto'
            params = {'chat_id':chatID, 'photo':photoURL}
            response = requests.get(endPoint, params=params)
            endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
            params = {'chat_id': chatID, 'text':photoEXP}
            response = requests.get(endPoint, params=params)
        else:
            endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
            params = {'chat_id': chatID, 'text': 'Дата введена в неправильном формате!! Правильный формат: ГГГГ-ММ-ДД'}
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


























