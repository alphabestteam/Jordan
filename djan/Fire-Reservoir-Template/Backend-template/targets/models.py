from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=100)
    attack_priority = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    enemy_organization = models.CharField(max_length=100)
    target_goal = models.CharField(max_length=100)
    was_target_destroyed = models.BooleanField(default=False)
    target_id = models.IntegerField(unique=True)