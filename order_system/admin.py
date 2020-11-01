from django.contrib import admin
from order_system.base import BaseModelAdmin, BaseModelTabularInlineAdmin
from order_system.models import Pizza, Order, OrderLine
# Register your models here.


admin.site.empty_value_display = '(empty)'

@admin.register(Pizza)
class PizzaAdmin(BaseModelAdmin):
  list_display = ('name', 'flavor', 'size', 'created_by', 'created_at', 'modified_by', 'modified_at')


class OrderLineInline(BaseModelTabularInlineAdmin):
  model = OrderLine


@admin.register(Order)
class OrderAdmin(BaseModelAdmin):
  list_display = ('customer_name', 'created_by', 'created_at', 'modified_by', 'modified_at')
  inlines = [
    OrderLineInline
  ]
  