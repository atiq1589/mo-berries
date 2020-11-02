from django.db import models
from order_system.base import BaseModel
from order_system.enums import OrderStatusEnum, PizzaFlavorEnum, PizzaSizeEnum
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

  flavor = models.CharField(
    verbose_name="Pizza Flavors",
    choices=PizzaFlavorEnum.to_tuple(), 
    max_length=15
  )

  size = models.CharField(
    verbose_name="Pizza Sizes",
    choices=PizzaSizeEnum.to_tuple(), 
    max_length=15
  )

  quantity = models.IntegerField(
    verbose_name="Order Quantity",
    validators=[MinValueValidator(1)],
  )

  def __str__(self):
    return '{0} - {1} - {2} - {3}'.format(self.order, self.flavor, self.size, self.quantity)

  class Meta:
    unique_together = (('order', 'flavor', 'size'),)

