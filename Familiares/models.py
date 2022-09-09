from django.db import models

# Create your models here.

class Padres (models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    sexo=models.CharField(max_length=1)
    fechaNac=models.DateField()
    dni=models.IntegerField()

class Familiar(models.Model):
    relacion=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    sexo=models.CharField(max_length=1)
    fechaNac=models.DateField()
    dni=models.IntegerField()
    materno=models.BooleanField()
    paterno=models.BooleanField()




