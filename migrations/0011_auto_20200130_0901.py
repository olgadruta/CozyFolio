# Generated by Django 2.2 on 2020-01-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozyfolio_app', '0010_auto_20200130_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='offerReject',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='response',
            field=models.IntegerField(),
        ),
    ]
