from django.db import models

class Person(models.Model):
    id_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Parent(Person):
    workplace = models.CharField(max_length=100, blank=True, null=True)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    children = models.ManyToManyField(Person, related_name='parents')
    def __str__(self):
        return self.name