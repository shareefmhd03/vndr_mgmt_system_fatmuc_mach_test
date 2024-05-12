from django.urls import path
from .views import *

urlpatterns = [
    path('',PurchaseOrderListCreate.as_view(),name = 'create-order-list'),
    path('<int:pk>',PurchaseOrderRetrieveUpdateDestroy.as_view(), name= 'ord-ret-upd-del'),
    path('<int:pk>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='ack-purchase-ord'),


]