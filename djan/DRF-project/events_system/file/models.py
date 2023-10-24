from django.db import models
from users.models import UserProfile
from events.models import BasicForm

class FileForm(models.Model):
    form = models.ForeignKey(BasicForm, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField()

    class Meta:
        app_label = 'file' 


 

