# Generated by Django 2.2 on 2020-01-30 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozyfolio_app', '0006_auto_20200129_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='averageRespond',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='mostPopularPortfolio',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='numbofJobApplied',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='offertReceived',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='offertReject',
            field=models.IntegerField(null=True),
        ),
    ]
