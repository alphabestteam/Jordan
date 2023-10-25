from django.db import models
author = models.CharField(max_length=50)


class Book(models.Model):
    
    title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    publication_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    #VALIDATE AUTHOR NAME FIELD
    def validate_author_name(value):
     special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
     for char in special_characters:
        if char in value:
            raise ValidationError("Author name cannot contain special characters.")

    def __str__(self):
        return self.title

