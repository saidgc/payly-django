from django.forms import ModelForm

from apps.services.models.service import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
