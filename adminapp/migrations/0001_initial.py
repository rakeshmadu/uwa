# Generated by Django 2.2.5 on 2019-09-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('Park_name', models.CharField(choices=[('Queen Elizabeth national park', 'Queen Elizabeth national park'), ('Murchison falls national park', 'Murchison falls national park'), ('Bwindi impenetrable national park', 'Bwindi impenetrable national park'), ('Lake Mburo national Park', 'Lake Mburo national Park'), ('Kidepo Valley National Park', 'Kidepo Valley National Park'), ('Semuliki National Park', 'Semuliki National Park'), ('Mt Elgon National Park', 'Mt Elgon National Park'), ('Mgahinga Gorilla National Park', 'Mgahinga Gorilla National Park')], max_length=50)),
                ('country', models.CharField(choices=[('Austria', 'Austria'), ('Bangladesh', 'Bangladesh'), ('Belize', 'Belize'), ('Canada', 'Canada'), ('Iceland', 'Iceland'), ('India', 'India'), ('Turkey', 'Turkey'), ('Uganda', 'Uganda')], max_length=50)),
                ('Email', models.EmailField(default='@gmail.com', max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TicketBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offline', models.CharField(choices=[('online_200', 'online_200'), ('offline_200', 'offline_200')], max_length=50)),
                ('online', models.CharField(choices=[('online_200', 'online_200'), ('offline_200', 'offline_200')], max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Date_of_visit', models.DateField(help_text='mm/dd/yyyy')),
                ('Time', models.CharField(choices=[('09:30 am to 10:30 am', '09:30 am to 10:30 am'), ('11:00 am to 12:00 pm', '11:00 am to 12:00 pm'), ('12:30 pm to 01:30 pm', '12:30 pm to 01:30 pm'), ('02:30 pm to 03:30 pm', '02:30 pm to 03:30 pm'), ('04:00 pm to 05:30 pm', '04:00 pm to 05:30 pm')], max_length=50)),
                ('Vehicle_No', models.CharField(max_length=50)),
                ('ticketprice', models.CharField(choices=[('Adult', (('Rs 80 ', 'Rs 80 '),)), ('Child', (('Rs 40 ', 'Rs 40 '),))], max_length=50)),
                ('Govt_id', models.CharField(choices=[('AadharNumber', 'AadharNumber'), ('pan_card', 'pan_card')], max_length=12)),
                ('id_Number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
