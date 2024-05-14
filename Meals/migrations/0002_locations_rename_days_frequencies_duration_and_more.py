# Generated by Django 5.0.6 on 2024-05-14 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='frequencies',
            old_name='days',
            new_name='duration',
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Meals.locations'),
        ),
    ]