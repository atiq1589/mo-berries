# Generated by Django 3.1.2 on 2020-11-01 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order_system.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25, verbose_name='Pizza Name')),
                ('flavor', models.CharField(choices=[('margarita', 'MARGARITA'), ('marinara', 'MARINARA'), ('salami', 'SALAMI')], default=order_system.enums.PizzaFlavorEnum['MARGARITA'], max_length=15, verbose_name='Pizza Flavors')),
                ('size', models.CharField(choices=[('small', 'SMALL'), ('medium', 'MEDIUM'), ('large', 'LARGE')], default=order_system.enums.PizzaSizeEnum['MEDIUM'], max_length=15, verbose_name='Pizza Sizes')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizza_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizza_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]