# Generated by Django 4.1.3 on 2022-11-17 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0025_rename_album_id_albumssongs_album_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='manager',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='jams.managers'),
        ),
    ]
