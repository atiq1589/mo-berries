from django.test import TestCase
from order_system.models import Order
from rest_framework.test import APIClient
from rest_framework import status


class OrderTestCase(TestCase):
  def setUp(self):
    self.client = APIClient(enforce_csrf_checks=False)

  def test_order_submit(self):
    """
    Test order create API
    """
    payload = dict(customer_name="Md. Atiqul Islam", customer_address="Dhaka, Bangladesh")

    response = self.client.post('/api/v1/orders/', payload, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Order.objects.count(), 1)
    self.assertEqual(Order.objects.last().customer_name, 'Md. Atiqul Islam')

  def test_get_order_list(self):
    """
    Test order list get API
    """
    order = Order.objects.create(customer_name="Md. Atiqul Islam", customer_address="Dhaka, Bangladesh")
    response = self.client.get('/api/v1/orders/', format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0].get('customer_name'), 'Md. Atiqul Islam')
