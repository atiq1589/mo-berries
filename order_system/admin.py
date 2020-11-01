from django.contrib import admin
from order_system.base import BaseModelAdmin
from order_system.models import Pizza
# Register your models here.


@admin.register(Pizza)
class PizzaAdmin(BaseModelAdmin):
  list_display = ('name', 'flavor', 'size', 'created_by', 'created_at', 'modified_by', 'modified_at')
