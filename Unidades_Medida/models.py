from django.db import models

# Create your models here.
class unidades(models.Model):
	Kilo = 'KG'
	Litro = 'LT'
	Unidad = 'UND'
	multiplica="x"
	divide="%"
	comportamiento = [(multiplica, "Multiplica"),(divide," Divide"),]
	lista = [
		(Kilo, "Kilo"),
        (Kilo, "Gramo"),
        (Litro, "Litro"),
        (Litro, "C.C"),
        (Unidad, "Unidad"),
        ]
	codigo = models.CharField(max_length=3,primary_key=True)
	Unidad = models.CharField(max_length=15,null=False)
	Unidad_Basica = models.CharField(max_length=2,choices=lista)
	Operador = models.CharField(max_length=3,choices=comportamiento)
	Factor=models.IntegerField(null=False,default=1)
	activo=models.BooleanField(null=False, default=True)
