"""payly2 URL Configuration

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
from django.urls import path

import auth_service.views as auth
import landing_page.views as landing_page
import services.views as services
import account.views as account

urlpatterns = [
    path('', landing_page.index),
    path('admin/', admin.site.urls),
    path('login/', auth.login_view),
    path('logout/', auth.logout_view),
    path('services/', services.show_all_services),
    path('pay', services.pay_service),
    path('account/', account.home),
]
