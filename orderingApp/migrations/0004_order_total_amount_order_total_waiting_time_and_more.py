# Generated by Django 4.0.5 on 2022-07-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderingApp', '0003_orderdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_waiting_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Orderdetails',
        ),
    ]
