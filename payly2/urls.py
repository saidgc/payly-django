"""payly2 URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.account import views as account
from apps.auth_service import views as auth
from collaborator import views as collaborator
from landing_page import views as landing_page
from services import views as services

urlpatterns = [
    path('', landing_page.index, name='landing'),
    path('warranty/', landing_page.index, name='warranty'),  # TODO

    path('admin/', admin.site.urls, name='admin'),

    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('forgot/', landing_page.index, name='forgot'),  # TODO
    path('register/', landing_page.index, name='register'),  # TODO

    path('services/', services.show_all_services, name='services'),
    path('pay', services.pay_service, name='service_pay'),

    path('account/', include([
        path('', account.home, name='account'),
        path('receipt/', account.receipts, name='account_receipts'),
    ])),

    path('collaborator/', include([
        # TODO create service menu for collaborator
        path('pay/', collaborator.pay_service_collaborator, name='collaborator_pay_service'),
        path('pay/<slug:service_id>', collaborator.pay_service_collaborator, name='collaborator_pay_service'),
        path('pay/<slug:service_id>/pay/', collaborator.process_order, name='collaborator_pay_service_pay'),
        path('receipts/', account.home, name='collaborator_receipts'),  # TODO
        path('due/', account.home, name='collaborator_due'),  # TODO
        path('payout/', account.home, name='collaborator_payout'),  # TODO
    ])),

    path('staff/payments', account.home, name='staff_payments'),  # TODO

    path('super/payments', account.home, name='super_payments'),  # TODO
    path('super/payout', account.home, name='super_payout'),  # TODO
]
