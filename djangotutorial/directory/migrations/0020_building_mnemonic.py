# Generated by Django 5.1.7 on 2025-04-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0019_building_has_ground_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='mnemonic',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
