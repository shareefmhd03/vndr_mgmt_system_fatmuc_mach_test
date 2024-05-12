
from django.http import Http404
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorPerformance(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            performance_data = {
                'on_time_delivery_rate': instance.on_time_delivery_rate,
                'quality_rating_avg': instance.quality_rating_avg,
                'average_response_time': instance.average_response_time,
                'fulfillment_rate': instance.fullfillment_rate,
            }
            return Response(performance_data)
        except Http404:
            return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)