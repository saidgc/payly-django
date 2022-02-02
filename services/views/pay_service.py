from django.shortcuts import render
from django.http import HttpResponseRedirect
from firebase_db.models.collections import Service


def pay_service(request):
    if request.method != "POST":
        return HttpResponseRedirect('/')

    service_id = request.POST.get('id', False)
    if not service_id:
        return HttpResponseRedirect('/services')
    service = Service().get_service(service_id=service_id)

    context = {
        'title': "Pagar " + service['name'],
        'id': service_id
    }
    context.update(service)
    return render(
        request=request,
        template_name='pay_service.html',
        context=context,
    )
