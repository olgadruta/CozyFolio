# Generated by Django 2.2 on 2020-01-26 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozyfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
