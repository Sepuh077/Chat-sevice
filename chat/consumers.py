from datetime import datetime
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .manager import create_text_message
from .thread import ChatThread
import time

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.room_group_name = 'chat_%s' % self.group_id

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        group_id = self.room_group_name.replace('chat_', '')
        replied_from = text_data_json['replied_from']
        thread = ChatThread(
            target=create_text_message, 
            args=(sender, group_id, message, replied_from)
        )
        thread.start()
        thread.join()
        # time.sleep(2)
        # msg_id = sync_to_async(create_text_message).func(sender, group_id, message, replied_from)
        # print(msg_id, type(msg_id))
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'id': text_data_json['id'],
                # 'id': msg_id
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        value_id = event['id']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'value_id': value_id
        }))
