from rest_framework import generics
from .models import Vendor
from store.models import PurchaseOrder

from .serializers import VendorSerializer
from store.serializers import PurchaseOrderSerializer

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer



