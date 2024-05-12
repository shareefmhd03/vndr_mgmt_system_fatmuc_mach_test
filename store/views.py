from time import timezone
from django.http import Http404

from rest_framework import generics, status
from rest_framework.response import Response

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset  = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset  = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class AcknowledgePurchaseOrder(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.acknowledgment_date = timezone.now()  # Assuming timezone is imported
            instance.save()
            return Response({'message': 'Purchase Order acknowledged successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
