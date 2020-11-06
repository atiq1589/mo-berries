from order_system.base.serializers import BaseModelSerializer
from order_system.models import Order, OrderLine
from rest_framework import serializers
from order_system.enums import OrderStatusEnum
from gettext import gettext as _


class OrderLineSerializer(BaseModelSerializer):
  """
  Order Line Serializer
  """
  def validate_order_status(self, order):
    if order.order_status == OrderStatusEnum.DELIVERED.value:
      raise serializers.ValidationError(_("Order Already Delivered. You can't change already delivered order."))

  def create(self, validated_data):
    order = validated_data.get('order')
    self.validate_order_status(order)
    return super().create(validated_data)

  def update(self, instance, validated_data):
    self.validate_order_status(instance.order)
    return super().update(instance, validated_data)

  class Meta:
    model = OrderLine
    exclude = ('created_by', 'modified_by', 'created_at', 'modified_at')


class OrderSerializer(BaseModelSerializer):
  """
  Order Serializer
  """
  order_line = serializers.PrimaryKeyRelatedField(many=True, queryset=OrderLine.objects.all(), required=False)

  def update(self, instance, validated_data):
    if instance.order_status == OrderStatusEnum.DELIVERED.value:
      raise serializers.ValidationError(_("Order Already Delivered. You can't change already delivered order."))

    return super().update(instance, validated_data)
    
  class Meta:
    model = Order
    exclude = ('created_by', 'modified_by', 'created_at', 'modified_at')