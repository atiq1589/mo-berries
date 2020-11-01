from django.db import models
from order_system.base import BaseModel
from order_system.enums import OrderStatusEnum
from django.core.validators import MinValueValidator


class OrderLine(BaseModel):
  """
  Order Line model
  """

  order = models.ForeignKey('order_system.order',
    verbose_name="Order",
    on_delete=models.CASCADE,
    related_name='order_line'
  )

  pizza = models.ForeignKey('order_system.pizza',
    verbose_name="Pizza",
    on_delete=models.PROTECT
  )

  quantity = models.IntegerField(
    verbose_name="Order Quantity",
    validators=[MinValueValidator(1)],
  )

  def __str__(self):
    return '{0} - {1} - {2}'.format(self.order, self.pizza, self.quantity)

  class Meta:
    unique_together = (('order', 'pizza'),)

