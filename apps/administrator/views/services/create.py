from django.shortcuts import redirect, render

from apps.services.models.service import Service


def create_services(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='administrator/services/create_service.html',
        context={'segment': 'services'},
    )
