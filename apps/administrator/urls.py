from django.urls import path, include
from apps.administrator.views import home as views

urlpatterns = [
    path('dashboards/', include([
        path('home/', views.home, name='administrator_dashboard_home'),
    ])),
    path('services/', include([
        path('show_all_services/', views.services, name='administrator_services_show_all'),
        path('create/', views.create_services, name='administrator_services_create'),
    ])),
    path('customers/', include([
        path('show_all_customers/', views.customers, name='administrator_customers_show_all'),
        path('create/', views.create_customers, name='administrator_customers_create'),
    ])),
    path('charges/', include([
        path('show_all_customers/', views.charges, name='administrator_charges_show_all'),
        path('create/', views.create_charge, name='administrator_charges_create'),
    ])),
]
