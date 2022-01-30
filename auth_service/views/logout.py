from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from firebase_db.models.authentication import FIREBASE_KEY


def logout_view(request):
    logout(request)
    request.session[FIREBASE_KEY] = ''
    return HttpResponseRedirect('/services')
