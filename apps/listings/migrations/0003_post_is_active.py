# Generated by Django 3.0.7 on 2020-09-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200907_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]