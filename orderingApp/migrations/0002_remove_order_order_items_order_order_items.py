# Generated by Django 4.0.5 on 2022-07-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderingApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(related_name='order_item', to='orderingApp.orderitem'),
        ),
    ]
