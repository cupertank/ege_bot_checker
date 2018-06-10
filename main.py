import telegram
import os
from telegram.ext import Updater
from requests import get
from time import sleep
if os.environ.get('TOKEN') != None:
    TOKEN = os.environ.get('TOKEN')
else:
    print('NO TOKEN!!!')
    exit()
updater = Updater(token=TOKEN)
bot = updater.bot
json = None
members = [163327661, '@egewithtay']
while json == None:
    try:
      json = get('http://check.ege.edu.ru/api/exam', cookies={'Participant':'634830F905CE5FF5D45969F63A4675D9FA54459F60C7699A1634B5E645CF3FA2743A8E25AE5C0215B082F703835F13A17880CF1AFD638D4DA00EAA11824BAC574A398FAE2C9EE04AA7C1B87BB1BC20C9D5F98251A64526B0B34A85C02A37F64F39A291A5'}).json()
    except:
      print('kek')
for mem in members:
    bot.send_message(chat_id=mem, text='РОБОТАЕТ')
json = json['Result'].copy()
while True:
    try:
       new_json = get('http://check.ege.edu.ru/api/exam', cookies={'Participant':'634830F905CE5FF5D45969F63A4675D9FA54459F60C7699A1634B5E645CF3FA2743A8E25AE5C0215B082F703835F13A17880CF1AFD638D4DA00EAA11824BAC574A398FAE2C9EE04AA7C1B87BB1BC20C9D5F98251A64526B0B34A85C02A37F64F39A291A5'}).json()
    except:
        print('kek')
    new_json = new_json['Result'].copy()
    if json != new_json:
        json = new_json.copy()
        for mem in members:
            bot.send_message(
                chat_id=mem,
                text='Что-то изменилось')
    sleep(60)
    
