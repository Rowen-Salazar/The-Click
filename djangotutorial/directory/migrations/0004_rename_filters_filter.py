# Generated by Django 5.1.5 on 2025-02-12 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_filters_map_building_delete_choice_delete_mapname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Filters',
            new_name='Filter',
        ),
    ]
