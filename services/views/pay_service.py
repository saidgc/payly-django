from django.shortcuts import redirect, render

from apps.firebase_db.models.collections import Service

TITLE = 'Pagar '


def pay_service(request):
    if request.method != 'POST':
        return redirect('landing')

    service_id = request.POST.get('id', '')
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
        template_name='pay_service.html',
        context=context,
    )
