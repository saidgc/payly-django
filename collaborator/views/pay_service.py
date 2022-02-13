from django.shortcuts import redirect, render

from firebase_db.models.collections import Service

TITLE = 'Pagar '


def pay_service_collaborator(request, service_id=None):
    if not request.user.is_authenticated:
        return redirect('login')

    if not service_id:
        return redirect('services')

    service = Service().get_service(service_id=service_id)

    context = {
        'title': TITLE + service['name'],
        'id': service_id,
    }
    context.update(service)
    return render(
        request=request,
        template_name='collaborator/services/telmex.html',
        context=context,
    )
