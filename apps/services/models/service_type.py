from django.db import models


class ServiceType(models.Model):
    name = models.CharField('Tipo de servicio', max_length=100)
