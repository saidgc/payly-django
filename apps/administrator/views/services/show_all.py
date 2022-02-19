from django.shortcuts import redirect, render

from apps.services.models.service import Service


def services(request):
    if not request.user.is_authenticated:
        return redirect('login')

    all_services = Service.objects.all()

    return render(
        request=request,
        template_name='administrator/services/services.html',
        context={'services': all_services},
    )
