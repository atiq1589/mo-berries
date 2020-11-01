from order_system.seralizers import OrderSerializer, OrderLineSerializer
from rest_framework import viewsets
from order_system.models import Order, OrderLine
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
  """
  Order View Set
  """

  queryset = Order.objects.all()
  serializer_class = OrderSerializer


class OrderLineViewSet(viewsets.ModelViewSet):
  """
  Order Line View Set
  """

  queryset = OrderLine.objects.all()
  serializer_class = OrderLineSerializer
