# Generated by Django 5.0.6 on 2024-05-25 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_phn', models.CharField(max_length=12)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.event')),
            ],
        ),
    ]
