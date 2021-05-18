# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RetailPrices(models.Model):
    idretail_prices = models.AutoField(primary_key=True)
    skuid = models.CharField(db_column='skuId', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='currencyCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tierminimumunits = models.IntegerField(db_column='tierMinimumUnits', blank=True, null=True)  # Field name made lowercase.
    retailprice = models.DecimalField(db_column='retailPrice', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='unitPrice', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    armregionname = models.CharField(db_column='armRegionName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=100, blank=True, null=True)
    effectivestartdate = models.CharField(db_column='effectiveStartDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    meterid = models.CharField(db_column='meterId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    metername = models.CharField(db_column='meterName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    productid = models.CharField(db_column='productId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    skuname = models.CharField(db_column='skuName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='serviceName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    serviceid = models.CharField(db_column='serviceId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    servicefamily = models.CharField(db_column='serviceFamily', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unitofmeasure = models.CharField(db_column='unitOfMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    retail_type = models.CharField(max_length=100, blank=True, null=True)
    isprimarymeterregion = models.CharField(db_column='isPrimaryMeterRegion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    armskuname = models.CharField(db_column='armSkuName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vmsizename = models.CharField(db_column='vmSizeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vmsizecpucores = models.IntegerField(db_column='vmSizeCpuCores', blank=True, null=True)  # Field name made lowercase.
    vmsizerammb = models.IntegerField(db_column='vmSizeRamMb', blank=True, null=True)  # Field name made lowercase.
    dt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retail_prices'