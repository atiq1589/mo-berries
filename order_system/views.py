from order_system.seralizers import OrderSerializer, OrderLineSerializer
from rest_framework import viewsets, filters
from order_system.models import Order, OrderLine
from django_filters.rest_framework import DjangoFilterBackend


class OrderViewSet(viewsets.ModelViewSet):
  """
  Order View Set
  """

  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
  search_fields = ['customer_name', 'customer_address',]
  filterset_fields = ('order_status',)


class OrderLineViewSet(viewsets.ModelViewSet):
  """
  Order Line View Set
  """

  queryset = OrderLine.objects.all()
  serializer_class = OrderLineSerializer
