# Generated by Django 4.2 on 2023-04-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0001_initial'),
        ('app_1', '0003_tuser_t'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuser',
            name='t',
        ),
        migrations.AddField(
            model_name='tuser',
            name='t',
            field=models.ManyToManyField(to='app_2.tposition'),
        ),
    ]
