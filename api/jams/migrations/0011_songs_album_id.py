# Generated by Django 4.1.3 on 2022-11-16 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0010_songs_is_explicit'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='album_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jams.albums'),
        ),
    ]
