# Generated by Django 4.1.3 on 2022-11-16 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0021_remove_artists_manager_artistsmanagers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArtistsManagers',
        ),
        migrations.DeleteModel(
            name='Managers',
        ),
    ]
