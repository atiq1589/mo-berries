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


class OrderStatusEnum(BaseEnum):
  """
  Define Order Status
  """

  PENDING = 'pending'
  CONFIRMED = 'confirmed'
  IN_PROGRESS = 'in_progress' 
  DELIVERED = 'delivered'
  CANCELED = 'canceled'
