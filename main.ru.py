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

#Функция дает гифку с ответом yes или no
def giveAnimation(answer: str) -> str:
    endPoint = f'https://yesno.wtf/api?force={answer}'
    res = requests.get(endPoint).json()
    return res['image']

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
        # if checkDate(userText):
        #     photoURL, photoEXP = givePhoto(userText)
        #     endPoint = f'https://api.telegram.org/bot{token}/sendPhoto'
        #     params = {'chat_id':chatID, 'photo':photoURL}
        #     response = requests.get(endPoint, params=params)
        #     endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
        #     params = {'chat_id': chatID, 'text':photoEXP}
        #     response = requests.get(endPoint, params=params)
        # else:
        #     endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
        #     params = {'chat_id': chatID, 'text': 'Дата введена в неправильном формате!! Правильный формат: ГГГГ-ММ-ДД'}
        #     response = requests.get(endPoint, params=params)
        endPoint = f'https://api.telegram.org/bot{token}/sendAnimation'
        params = {'chat_id':chatID, 'animation': giveAnimation(userText)}
        response = requests.get(endPoint, params=params)
    time.sleep(1)


































