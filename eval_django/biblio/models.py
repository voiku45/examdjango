from django.db import models
from django.utils import timezone

class Livres(models.Model):
	auteur = models.CharField(max_length=100)
	titre = models.CharField(max_length=25)
	annee = models.DateTimeField()
	#image = models.ImageField(upload_to='images/')
# Create your models here.
