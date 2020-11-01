from order_system.base import BaseEnum


class PizzaFlavorEnum(BaseEnum):
  """
  Define Pizza Flavor
  """

  MARGARITA = 'margarita' 
  MARINARA = 'marinara' 
  SALAMI = 'salami'


class PizzaSizeEnum(BaseEnum):
  """
  Define Pizza Size
  """

  SMALL = 'small' 
  MEDIUM = 'medium' 
  LARGE = 'large'
  