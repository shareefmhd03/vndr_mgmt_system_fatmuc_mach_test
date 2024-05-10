from django.db import models
from vendor.models import Vendor
# Create your models here.
class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('completed','Completed'),
        ('canceled','Canceled')
    )

    po_number     = models.CharField(max_length=50,unique=True)
    vendor        = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date    = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items    = models.JSONField()
    quantity = models.IntegerField()
    status   = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    quality_rating     = models.FloatField(blank=True,null=True)
    issue_date         = models.DateTimeField(auto_now_add=True)
    acknowlegment_date = models.DateTimeField(blank=True,null=True)

    def __str__(self) -> str:
        return str(self.po_number)
    
