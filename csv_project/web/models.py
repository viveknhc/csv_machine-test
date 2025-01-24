from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name