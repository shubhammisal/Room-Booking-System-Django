# Generated by Django 4.0.3 on 2022-05-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_end_day_alter_booking_start_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_day',
            field=models.DateField(),
        ),
    ]
