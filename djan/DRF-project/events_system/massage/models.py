from django.db import models
from users.models import UserProfile
from events.models import BasicForm

class Chat(models.Model):
    chat_id =models.IntegerField(primary_key=True)

     
class ChatMassage(models.Model):
    form = models.ForeignKey(BasicForm, on_delete=models.CASCADE)
    text = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_messages')

    class Meta:
        app_label = 'massage' 

        
