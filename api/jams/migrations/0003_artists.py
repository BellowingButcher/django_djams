# Generated by Django 4.1.3 on 2022-11-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0002_songs_duration_songs_plays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
