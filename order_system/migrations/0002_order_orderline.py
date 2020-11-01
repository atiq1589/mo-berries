# Generated by Django 3.1.2 on 2020-11-01 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order_system.enums


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('customer_name', models.CharField(max_length=50, verbose_name='Customer Name')),
                ('customer_address', models.TextField(verbose_name='Customer Address')),
                ('order_status', models.CharField(choices=[('pending', 'PENDING'), ('confirmed', 'CONFIRMED'), ('in_progress', 'IN_PROGRESS'), ('delivered', 'DELIVERED'), ('canceled', 'CANCELED')], default=order_system.enums.OrderStatusEnum['PENDING'], max_length=15, verbose_name='Order Status')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(verbose_name='Order Quantity')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderline_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderline_modified_by', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_system.order', verbose_name='Order')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_system.pizza', verbose_name='Pizza')),
            ],
            options={
                'unique_together': {('order', 'pizza')},
            },
        ),
    ]