from django.db import models

class Roles(models.Model):
	name = models.CharField(max_length=100)    
 
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=7)
    rol = models.ForeignKey(Roles)
            