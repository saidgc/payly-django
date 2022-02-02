from django.shortcuts import render
from firebase_db.models.collections import Service


def show_all_services(request):
    services = Service().get_all_services()

    context = {
        'title': "Inicio",
        'services': services,
    }
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )
