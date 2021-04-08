from django.db import models

# Create your models here.

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length= 2000)
    date = models.DateTimeField('date published')
    email = models.EmailField(max_length = 254)
    name = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.name
