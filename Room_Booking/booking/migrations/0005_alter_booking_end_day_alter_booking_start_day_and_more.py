# Generated by Django 4.0.3 on 2022-05-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_payment_payment_type_alter_booking_room_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_day',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_day',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Payment_date',
            field=models.DateField(auto_now=True),
        ),
    ]
