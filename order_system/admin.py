from django.contrib import admin
from order_system.base import BaseModelAdmin, BaseModelTabularInlineAdmin
from order_system.models import Order, OrderLine
# Register your models here.


admin.site.empty_value_display = '(empty)'


class OrderLineInline(BaseModelTabularInlineAdmin):
  model = OrderLine


@admin.register(Order)
class OrderAdmin(BaseModelAdmin):
  list_display = ('customer_name', 'created_by', 'created_at', 'modified_by', 'modified_at')
  inlines = [
    OrderLineInline
  ]
  