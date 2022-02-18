from django.urls import path, include
from apps.administrator import views

urlpatterns = [
    path('dashboards/', include([
        path('home/', views.home, name='administrator_dashboard_home'),
    ])),
    path('services/', include([
        path('show_all_services/', views.services, name='administrator_services_show_all'),
    ])),
]
