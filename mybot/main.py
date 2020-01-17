from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time

token = "0ed166a31bd5349dbb24da812449f9ce341cbaf3c8cfeefd7529fcfc43f1ddda45df625c6d8c25fc2f8b5"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "Привет":
                    vk_session.method('messages.send', {'used_id': event.user_id, 'message': 'Привет, друг! ', 'random_id': 0})

