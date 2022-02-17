from django.shortcuts import redirect

from apps.collaborator.forms.telmex_form import TelmexForm
from apps.firebase_db.models.collections import Service, Payment

TITLE = 'Pagar '


def process_order(request, service_id=None):
    if request.method == 'POST':
        requested_form = TelmexForm(request.POST)
        if requested_form.is_valid():
            print(requested_form)
            # Payment().collection.set({
            #     'user': userId,
            #     'user_ip': user_ip,
            #     'payment_date': datetime.now(),
            #     'payment_data': data,
            #     'payment_completed': False,
            #     'completed': False,
            #     'authorization': '',
            #     'problem': False,
            #     'discount': service_discount,
            #     'payment_method': 'Paypal'
            # })

    return redirect('account')
