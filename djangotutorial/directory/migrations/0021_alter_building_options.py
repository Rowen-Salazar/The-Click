# Generated by Django 5.1.7 on 2025-04-10 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0020_building_mnemonic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['display_name']},
        ),
    ]
