# Generated by Django 2.2.5 on 2019-09-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20190907_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='ONLINE', editable=False, max_length=7),
        ),
    ]
