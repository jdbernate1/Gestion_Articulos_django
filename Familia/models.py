from django.db import models

# Create your models here.

class Familia(models.Model):
	codigo = models.CharField(max_length=4,primary_key=True,null=False)
	Nombre = models.CharField(max_length=20,null=False)
	activo = models.BooleanField(default=True)

