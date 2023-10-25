from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField()
    unread_messages = models.ManyToManyField(to= 'massage.ChatMassage', related_name='unread_for')

    def add_unread_message(self, massage):
        if not massage.is_read:
            self.unread_messages.add(massage)

    def mark_message_as_read(self, message):
            if message in self.unread_messages.all():
                self.unread_messages.remove(message)
                message.is_read = True
                message.save()

    class Meta:
        app_label = 'users' 
