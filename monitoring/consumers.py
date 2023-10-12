import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class TaskProgressConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = 'task_progress'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            progress = text_data_json['progress']
            task_id = text_data_json['task_id']

            # 数据验证
            if not 0 <= progress <= 100:
                raise ValueError("Invalid progress value")
            
                    # Broadcast progress to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'task_progress',
                    'progress': progress,
                    'task_id': task_id
                }
            )
        except Exception as e:
            await self.send(text_data=json.dumps({'error': str(e)}))

    async def task_progress(self, event):
        progress = event['progress']
        task_id = event['task_id']

        await self.send(text_data=json.dumps({
            'task_id': task_id,
            'progress': progress
        }))
