# Generated by Django 2.2.5 on 2019-09-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticket_id', models.PositiveIntegerField(default='6565')),
                ('Date', models.DateField()),
                ('Vistorname', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=30)),
                ('TimeSlot', models.CharField(choices=[('09:30 am to 10:30 am', '09:30 am to 10:30 am'), ('11:00 am to 12:00 pm', '11:00 am to 12:00 pm'), ('12:30 pm to 01:30 pm', '12:30 pm to 01:30 pm'), ('02:30 pm to 03:30 pm', '02:30 pm to 03:30 pm'), ('04:00 pm to 05:30 pm', '04:00 pm to 05:30 pm')], max_length=50)),
                ('Vehicle_No', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('ticketprice', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employ_id', models.PositiveIntegerField(default='8969')),
                ('Employ_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=30)),
                ('contact_number', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
            ],
        ),
    ]
