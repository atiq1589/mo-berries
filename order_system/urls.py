from order_system.views import OrderViewSet, OrderLineViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-lines', OrderLineViewSet, basename='order-line')

urlpatterns = [
    path('', include(router.urls)),
]

