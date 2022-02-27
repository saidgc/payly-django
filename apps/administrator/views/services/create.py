from django.shortcuts import redirect, render

from apps.services.forms.form import ServiceForm
from apps.services.models.service import Service


def create_services(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        request_form = ServiceForm(request.POST)
        service = Service(**request_form.cleaned_data)
        service.save()
        redirect('administrator_services_show_all')

    return render(
        request=request,
        template_name='administrator/services/create_service.html',
        context={
            'segment': 'services',
            'service_form': ServiceForm()
        },
    )
