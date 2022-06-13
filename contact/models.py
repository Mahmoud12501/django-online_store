from django.db import models

# Create your models here.
class Send_Message(models.Model):
    email=models.EmailField(max_length=254)
    massage=models.TextField(max_length=1000)
    def __str__(self) :
        return self.name