from django.contrib import admin

from apps.services.models.service import Service
from apps.services.models.service_type import ServiceType

admin.site.register(ServiceType)
admin.site.register(Service)
