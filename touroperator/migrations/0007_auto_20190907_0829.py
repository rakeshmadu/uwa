# Generated by Django 2.2.5 on 2019-09-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touroperator', '0006_auto_20190907_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Ticket_id',
            field=models.PositiveIntegerField(default='6077'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Employ_id',
            field=models.PositiveIntegerField(default='7500'),
        ),
    ]