from django.db import models
from order_system.base import BaseModel
from order_system.enums import OrderStatusEnum


class Order(BaseModel):
  """
  Order model
  """

  customer_name = models.CharField(
    verbose_name="Customer Name",
    max_length=50
  )

  customer_address = models.TextField(
    verbose_name="Customer Address"
  )

  order_status = models.CharField(
    verbose_name="Order Status",
    choices=OrderStatusEnum.to_tuple(), 
    default=OrderStatusEnum.PENDING,
    max_length=15
  )

  def __str__(self):
    return '{0} - {1}'.format(self.customer_name, self.order_status)

