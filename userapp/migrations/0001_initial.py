# Generated by Django 2.2.5 on 2019-09-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('mobileno', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('parks_names', models.CharField(choices=[('Queen Elizabeth national park', 'Queen Elizabeth national park'), ('Murchison falls national park', 'Murchison falls national park'), ('Bwindi impenetrable national park', 'Bwindi impenetrable national park'), ('Lake Mburo national Park', 'Lake Mburo national Park'), ('Kidepo Valley National Park', 'Kidepo Valley National Park'), ('Semuliki National Park', 'Semuliki National Park'), ('Mt Elgon National Park', 'Mt Elgon National Park'), ('Mgahinga Gorilla National Park', 'Mgahinga Gorilla National Park')], max_length=35)),
                ('cost', models.CharField(max_length=10)),
                ('total', models.IntegerField()),
                ('child', models.IntegerField()),
                ('adult', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=20)),
                ('idproof', models.CharField(max_length=30)),
                ('idno', models.CharField(max_length=15)),
                ('vehicle_no', models.CharField(max_length=6)),
                ('reg_id', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('ONLINE', 'online'), ('OFFLINE', 'offline')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
