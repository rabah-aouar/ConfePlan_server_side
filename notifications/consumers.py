import json
from multiprocessing.sharedctypes import Value
from channels.generic.websocket import WebsocketConsumer
from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer
from notifications.NotificationSerializer import NotificationSerializer
from asgiref.sync import async_to_sync
class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name='test'
        self.room_groupe_name=self.scope['user'].id
        print(self.room_groupe_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_groupe_name,
            self.channel_name
        )
        self.accept()
        user=UserProfileModificationSerializer(self.scope['user']).data
        notifications=NotificationSerializer(data=self.scope['user'].notification_set.all(),many=True)
        notifications.is_valid()
        notifications_data=notifications.data
        self.send(text_data=json.dumps({'notifications':notifications_data,}))
    def receive(self, text_data=None, bytes_data=None):
        return super().receive(text_data, bytes_data)

    def disconnect(self, code):
        return super().disconnect(code)

    def send_notification(self,event):
        self.send(text_data=json.dumps({'notifications':[json.dumps(NotificationSerializer(event["value"]).data),]}))