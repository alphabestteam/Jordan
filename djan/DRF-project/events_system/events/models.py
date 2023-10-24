from django.db import models
from users.models import UserProfile

class BasicForm(models.Model):
    reporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[("open", "Open"), ("closed", "Closed"), ("pending", "Pending"), ("waiting", "Waiting")])
    is_draft = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    shared_users = models.ManyToManyField(UserProfile, related_name="shared_forms")

    class Meta:
        app_label = 'events' 






