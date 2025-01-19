# Generated by Django 4.2 on 2025-01-19 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('level', models.IntegerField()),
                ('date_birth', models.DateField()),
                ('picture', models.ImageField(upload_to='trainer_images')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('F', 'Fuego'), ('E', 'Electrico'), ('A', 'Agua'), ('P', 'Planta'), ('L', 'Lagartija'), ('T', 'Tierra')], max_length=30)),
                ('weight', models.DecimalField(decimal_places=4, max_digits=6)),
                ('height', models.DecimalField(decimal_places=4, max_digits=6)),
                ('picture', models.ImageField(upload_to='pokemons_images')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokedex.trainer')),
            ],
        ),
    ]
