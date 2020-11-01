# Generated by Django 3.1.2 on 2020-11-01 14:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0002_order_orderline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_line', to='order_system.order', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Order Quantity'),
        ),
    ]
