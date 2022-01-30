from django.shortcuts import render
from firebase_db.models.collections import Collections


def index(request):
    services = Collections().get_all_services()
    # session['saveForm'] = False
    # try:
    #     isAuth = session['idToken']
    # except:
    #     isAuth = None

    context = {
        'title': "Inicio",
        'services': services,
        'isAuth': None
    }
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )
