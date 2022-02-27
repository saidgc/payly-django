from django.db import models

from apps.services.models.service_type import ServiceType


class Service(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT)
    description = models.TextField('Descripción', max_length=1000, null=True)
    name = models.CharField('Nombre del servicio', max_length=100)
    # currency = models.ManyToManyField(Currency)
    base_discount = models.DecimalField('Descuento base del servicio', decimal_places=2, max_digits=99)
    identifier_name = models.CharField('Identificador del servicio (Número, Cuenta, etc)', max_length=100, null=True)
    identifier_length = models.IntegerField('Longitud del identificador', null=True)
    additional_identifier = models.JSONField('Identificadores adicionales', null=True)
    SKU = models.CharField('SKU', max_length=20)
    status = models.BooleanField('Status', default=False)
    icon = models.ImageField('Imagen del servicio', null=True)
