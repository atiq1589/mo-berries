from order_system.base.serializers import BaseModelSerializer
from order_system.models import Order, OrderLine
from rest_framework import serializers


class OrderLineSerializer(BaseModelSerializer):
  """
  Order Line Serializer
  """
  class Meta:
    model = OrderLine
    exclude = ('created_by', 'modified_by', 'created_at', 'modified_at')


class OrderSerializer(BaseModelSerializer):
  """
  Order Serializer
  """
  order_line = serializers.PrimaryKeyRelatedField(many=True, queryset=OrderLine.objects.all())
  class Meta:
    model = Order
    exclude = ('created_by', 'modified_by', 'created_at', 'modified_at')