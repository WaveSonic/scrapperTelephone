from telethon.sync import TelegramClient
import csv
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 24675629
api_hash = '9869a9ffa918b3f265534007f073efcf'
phone = '+380963049117'

client = TelegramClient(phone, api_id, api_hash)
client.start()

chats = []
last_date = None
size_chats = 200
groups=[]

result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=size_chats,
            hash = 0
        ))
chats.extend(result.chats)

for chat in chats:
   try:
       if chat.megagroup== True:
           groups.append(chat)
   except:
       continue

print('Выберите номер группы из перечня:')
i=0
for g in groups:
   print(str(i) + '- ' + g.title)
   i+=1

g_index = input("Введите нужную цифру: ")
target_group=groups[int(g_index)]

print('Узнаём пользователей...')
all_participants = []
all_participants = client.get_participants(target_group)
print(all_participants)

print('Сохраняем данные в файл...')
with open("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash'])
    for user in all_participants:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.id:
            user_id = user.id
        else:
            user_id = ""
        if user.access_hash:
            access_hash = user.access_hash
        else:
            access_hash = ""
        if user.phone:
            phone = user.phone
        else:
            phone = ""
        writer.writerow([username, user_id, access_hash])
print('Парсинг участников группы успешно выполнен.')



