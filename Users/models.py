from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50)
    role=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name