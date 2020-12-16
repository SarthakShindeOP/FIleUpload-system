from django.db import models

# Create your models here.

class login(models.Model):
    Username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self): 
         return self.Username
class Savedfile(models.Model):
    Username = models.CharField(max_length=30)
    file = models.FileField(upload_to='file')
    
    def __str__(self): 
         return self.Username
