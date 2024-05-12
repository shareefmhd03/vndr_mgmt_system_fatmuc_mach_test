from django.urls import path
from .views import *

urlpatterns = [
    path('',VendorListCreate.as_view(),name = 'create-ven-list'),
    path('<int:pk>',VendorRetrieveUpdateDestroy.as_view(), name= 'ven-ret-upd-del'),
    path('<int:pk>/performance/', VendorPerformance.as_view(), name='ven-performance'),


]