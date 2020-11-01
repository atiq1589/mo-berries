from django.db import models
from order_system.base import BaseModel
from order_system.enums import PizzaFlavorEnum, PizzaSizeEnum


class Pizza(BaseModel):
  """
  Pizza model
  """

  name = models.CharField(
    verbose_name="Pizza Name",
    max_length=25
  )

  flavor = models.CharField(
    verbose_name="Pizza Flavors",
    choices=PizzaFlavorEnum.to_tuple(), 
    default=PizzaFlavorEnum.MARGARITA,
    max_length=15
  )

  size = models.CharField(
    verbose_name="Pizza Sizes",
    choices=PizzaSizeEnum.to_tuple(), 
    default=PizzaSizeEnum.MEDIUM,
    max_length=15
  )

  def __str__(self):
    return '{0} - {1} - {2}'.format(self.name, self.flavor, self.size)

