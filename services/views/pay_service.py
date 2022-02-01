from django.shortcuts import render
from django.http import HttpResponseRedirect
from firebase_db.models.authentication import FIREBASE_KEY
from firebase_db.models.collections import Collections


def pay_service(request):
    if request.method != "POST":
        return HttpResponseRedirect('/')

    is_user_authenticated = None
    if request.user.is_authenticated:
        is_user_authenticated = request.session[FIREBASE_KEY]

    service_id = request.POST.get('id', False)
    if not service_id:
        return HttpResponseRedirect('/services')
    service = Collections().get_service(service_id=service_id)

    context = {
        'title': "Pagar " + service['name'],
        'is_user_authenticated': is_user_authenticated,
        'id': service_id
    }
    context.update(service)
    return render(
        request=request,
        template_name='pay_service.html',
        context=context,
    )
