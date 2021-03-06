import time

from django.shortcuts import redirect, render

from apps.firebase_db.models.collections import Payment


def receipts(request):
    if not request.user.is_authenticated:
        return redirect('login')

    customer_receipts = Payment().get_payments_by_customer(
        customer_id=request.user.firebase_user_id,
    )

    context = {
        'title': 'Recibos',
        'receipts': customer_receipts,
        'time': time,
    }
    return render(
        request=request,
        template_name='account/receipts.html',
        context=context,
    )
