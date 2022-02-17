from django.db import models

from apps.account.models import PaylyUser
from services.models.base_service import Service


class Customer(models.Model):
    name = models.CharField('Nombre', max_length=100)
    whatsapp_number = models.CharField('Whatsapp', max_length=15)
    email = models.EmailField('Correo electrónico')


class CollaboratorServicePay(models.Model):
    collaborator = models.ManyToManyField(PaylyUser)
    service = models.ManyToManyField(Service)
    customer = models.ManyToManyField(Customer)
    amount = models.DecimalField('Monto del pago', decimal_places=2, max_digits=999)
    discount = models.FloatField('Descuento del pago')
