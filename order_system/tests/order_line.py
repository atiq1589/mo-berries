from django.test import TestCase
from order_system.models import OrderLine, Order
from rest_framework.test import APIClient
from rest_framework import status
from order_system.enums import PizzaSizeEnum, PizzaFlavorEnum, OrderStatusEnum


class OrderLineTestCase(TestCase):
  def setUp(self):
    self.client = APIClient(enforce_csrf_checks=False)
    self.order = Order.objects.create(customer_name="Md. Atiqul Islam", customer_address="Dhaka, Bangladesh")
    self.delivered_order = Order.objects.create(customer_name="Md. Atiqul Islam", customer_address="Dhaka, Bangladesh", \
      order_status=OrderStatusEnum.DELIVERED.value)

  def test_order_line_create(self):
    """
    Test order create API
    """
    payload = dict(flavor=PizzaFlavorEnum.MARINARA.value, size=PizzaSizeEnum.LARGE.value, quantity=1, order=self.order.id)

    response = self.client.post('/api/v1/order-lines/', payload, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(OrderLine.objects.count(), 1)
    self.assertEqual(OrderLine.objects.last().flavor, PizzaFlavorEnum.MARINARA.value)
    self.assertEqual(OrderLine.objects.last().size, PizzaSizeEnum.LARGE.value)

  def test_get_order_lines(self):
    """
    Test order list get API
    """
    payload = dict(flavor=PizzaFlavorEnum.MARINARA.value, size=PizzaSizeEnum.LARGE.value, quantity=1, order=self.order)

    order_line = OrderLine.objects.create(**payload)
    response = self.client.get('/api/v1/order-lines/', format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0].get('flavor'), PizzaFlavorEnum.MARINARA.value)
    self.assertEqual(response.data[0].get('size'), PizzaSizeEnum.LARGE.value)
    self.assertEqual(response.data[0].get('quantity'), 1)

  def test_add_order_line_in_delivered_order(self):
    payload = dict(flavor=PizzaFlavorEnum.MARINARA.value, size=PizzaSizeEnum.LARGE.value, quantity=1, order=self.delivered_order.id)

    response = self.client.post('/api/v1/order-lines/', payload, format='json')

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(OrderLine.objects.count(), 0)
