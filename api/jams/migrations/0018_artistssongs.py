# Generated by Django 4.1.3 on 2022-11-16 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0017_albumssongs_album_id_alter_albumssongs_song_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistsSongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jams.artists')),
                ('song_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jams.songs')),
            ],
        ),
    ]
