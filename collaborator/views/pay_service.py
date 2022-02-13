from django.shortcuts import redirect, render

from collaborator.forms.telmex_form import TelmexForm
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
        'pay_form': TelmexForm(),
    }
    context.update(service)
    return render(
        request=request,
        template_name='collaborator/pay_service_base.html',
        context=context,
    )
