# Generated by Django 4.0.5 on 2022-07-02 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderingApp', '0002_remove_order_order_items_order_order_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_waiting_time', models.DurationField()),
                ('total_amount', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='orderingApp.order')),
            ],
        ),
    ]