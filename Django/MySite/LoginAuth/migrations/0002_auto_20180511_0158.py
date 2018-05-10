# Generated by Django 2.0.3 on 2018-05-10 17:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LoginAuth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='token_last_modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 10, 17, 58, 41, 725359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pass_word',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_token',
            field=models.CharField(max_length=64),
        ),
    ]
