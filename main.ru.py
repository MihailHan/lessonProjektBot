import requests
import pprint

with open('token.txt') as f:
    token = f.read()

# endPoint = f'https://api.telegram.org/bot{token}/getMe'
# res = requests.get(endPoint).json()
# pprint.pprint(res)

endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
res = requests.get(endPoint).json()
pprint.pprint(res)
chatID = res['result'][0]['message']['chat']['id']
print(chatID)
endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
params = {'chat_id':chatID, 'text': "Приветствую вас!"}
res = requests.get(endPoint, params=params).json()