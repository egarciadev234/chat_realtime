from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name'] #Obtiene el nombre de la sala (room_name) de la ruta URL en el archivo routing.py
        self.room_group_name = 'chat_%s' % self.room_name #Construye un nombre de grupo de canales desde el nombre de la habitacion especifada por el usuario

        async_to_sync(self.channel_layer.group_add)(
            #Se une al grupo 
            self.room_group_name,
            self.channel_name
        )
        self.accept() # Acepta la conexion WebSocket

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            #Deja el grupo
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            #Envia un evento al grupo
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
    }))