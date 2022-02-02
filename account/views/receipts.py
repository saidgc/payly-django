from django.http import HttpResponseRedirect
from django.shortcuts import render
from firebase_db.models.collections import Collections
import time


def receipts(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    customer_receipts = Collections.get_payments_by_customer()
    request.session[FIREBASE_KEY]

    context = {
        'title': "Recibos",
        'receipts': customer_receipts,
        'time': time,
    }
    return render(
        request=request,
        template_name='receipts.html',
        context=context,
    )
