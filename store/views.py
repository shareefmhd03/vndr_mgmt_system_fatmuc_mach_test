from rest_framework import generics

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset  = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset  = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer