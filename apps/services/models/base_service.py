from django.db import models


class ServiceType(models.Model):
    name = models.CharField('Tipo de servicio', max_length=100)


class Service(models.Model):
    service_type = models.ManyToManyField(ServiceType)
    name = models.CharField('Nombre del servicio', max_length=100)
    base_discount = models.DecimalField('Descuento base del servicio', decimal_places=2, max_digits=99)
    identifier_name = models.CharField('Identificador del servicio (Número, Cuenta, etc)', max_length=100)
    identifier_length = models.IntegerField('Longitud del identificador')
    additional_identifier = models.JSONField('Identificadores adicionales')
    # image = models.ImageField('Imagen del servicio')  # TODO install pillow
