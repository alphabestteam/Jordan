from django.db import models
from users.models import UserProfile
from events.models import BasicForm

class Chat(models.Model):
    chat_id =models.IntegerField(max_length=20, primary_key=True)

class ChatMessage(models.Model):
    form = models.ForeignKey(BasicForm, on_delete=models.CASCADE)
    text = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    class Meta:
        app_label = 'message' 