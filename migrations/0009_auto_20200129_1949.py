# Generated by Django 2.2 on 2020-01-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozyfolio_app', '0008_auto_20200129_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='numbofCompanyApplied',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='offerReject',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
