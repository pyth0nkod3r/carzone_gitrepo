# Generated by Django 3.2.8 on 2021-10-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_team_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photos',
            field=models.ImageField(upload_to='photo/%Y/%m/%d'),
        ),
    ]
