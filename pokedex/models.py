from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length = 25, null = False)
    last_name = models.CharField(max_length = 25, null = False)
    level = models.IntegerField()
    date_birth = models.DateField()
    picture = models.ImageField(upload_to="trainer_images")
    
    def __str__(self):
        return self.name +" "+self.last_name

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
    trainer = models.ForeignKey(Trainer, on_delete = models.SET_NULL, null=True)
    picture = models.ImageField(upload_to="pokemons_images")
    
    def __str__(self):
        return self.name

# Creacion del modelo TRAINER

    