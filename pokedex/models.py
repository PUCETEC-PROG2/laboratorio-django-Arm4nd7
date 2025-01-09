from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length = 30, null = False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Electrico'),
        ('L', 'Lagartija')
    }
    type = models.CharField(max_length = 30, null = False, choices=POKEMON_TYPES)
    weight = models.DecimalField(decimal_places = 4, max_digits = 6)
    height = models.DecimalField(decimal_places = 4, max_digits = 6)
    
    def __str__(self):
        return self.name

# Creacion del modelo TRAINER
class Trainer(models.Model):
    name = models.CharField(max_length = 25, null = False)
    last_name = models.CharField(max_length = 25, null = False)
    level = models.IntegerField()
    date_birth = models.DateField()
    
    def __str__(self):
        return self.name +" "+self.last_name
    