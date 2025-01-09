# Generated by Django 4.2 on 2025-01-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('weight', models.DecimalField(decimal_places=4, max_digits=6)),
                ('height', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
    ]
