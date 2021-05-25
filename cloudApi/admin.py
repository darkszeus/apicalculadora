from django.contrib import admin
from cloudApi.models import AzurePrices, AmazonPrices, RetailPrices
# Register your models here.

admin.site.register(AzurePrices)
admin.site.register(AmazonPrices)
admin.site.register(RetailPrices)
