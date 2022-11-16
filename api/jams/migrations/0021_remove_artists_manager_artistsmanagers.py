# Generated by Django 4.1.3 on 2022-11-16 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0020_artists_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artists',
            name='manager',
        ),
        migrations.CreateModel(
            name='ArtistsManagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.artists')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.managers')),
            ],
        ),
    ]
