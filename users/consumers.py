import json
import base64
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

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

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        image_data = text_data_json.get('image_data')  # Base64 encoded image data
        video_data = text_data_json.get('video_data')  # Base64 encoded video data
        username = text_data_json.get('username')

        if message:
            # Send text message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat.message',
                    'message': message,
                    'username': username,
                }
            )

        if image_data:
            # Handle image data (base64 encoded) and send to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat.image',
                    'image_data': image_data,
                    'username': username,
                }
            )

        if video_data:
            # Handle video data (base64 encoded) and send to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat.video',
                    'video_data': video_data,
                    'username': username,
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send text message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'type': 'text_message',
        }))

    async def chat_image(self, event):
        image_data = event['image_data']
        username = event['username']

        # Send image data to WebSocket
        await self.send(text_data=json.dumps({
            'image_data': image_data,
            'username': username,
            'type': 'image_message',
        }))

    async def chat_video(self, event):
        video_data = event['video_data']
        username = event['username']

        # Send video data to WebSocket
        await self.send(text_data=json.dumps({
            'video_data': video_data,
            'username': username,
            'type': 'video_message',
        }))

