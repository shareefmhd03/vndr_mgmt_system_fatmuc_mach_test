from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, F, ExpressionWrapper, fields
from django.db import models

from .models import Vendor
from store.models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, created, **kwargs):
    if instance.status == 'completed' and instance.vendor:
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
        on_time_delivered = completed_orders.filter(delivery_date__lte=instance.delivery_date).count()
        total_completed_orders = completed_orders.count()

        if total_completed_orders > 0:
            instance.vendor.on_time_delivery_rate = (on_time_delivered / total_completed_orders) * 100
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, created, **kwargs):
    if instance.status == 'completed' and instance.vendor and instance.quality_rating is not None:
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed').exclude(quality_rating__isnull=True)
        total_completed_orders = completed_orders.count()
        quality_ratings_sum = completed_orders.aggregate(models.Sum('quality_rating'))['quality_rating__sum']

        if total_completed_orders > 0:
            instance.vendor.quality_rating_avg = quality_ratings_sum / total_completed_orders
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    if instance.acknowledgment_date and instance.vendor:
        avg_response_time = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).aggregate(avg_response_time=Avg(ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=fields.DurationField())))
        
        if avg_response_time['avg_response_time']:
            instance.vendor.average_response_time = avg_response_time['avg_response_time'].total_seconds() / 60  # convert to minutes
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, created, **kwargs):
    if instance.vendor:
        fulfilled_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
        successful_fulfillments = fulfilled_orders.exclude(issue_date__isnull=True).exclude(acknowledgment_date__isnull=True).count()

        if fulfilled_orders.count() > 0:
            instance.vendor.fulfillment_rate = (successful_fulfillments / fulfilled_orders.count()) * 100
            instance.vendor.save()