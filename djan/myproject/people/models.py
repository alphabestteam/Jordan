from django.db import models

class Person(models.Model):
    id_number = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    city = models.CharField(max_length=100)

    class Meta:
        app_label = 'people'  