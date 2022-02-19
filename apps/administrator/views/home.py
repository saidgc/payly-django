from django.shortcuts import redirect, render

from apps.services.models.service import Service


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='administrator/home/index.html',
        context={'segment': 'index'},
    )


def services(request):
    if not request.user.is_authenticated:
        return redirect('login')

    all_services = Service.objects.all()

    return render(
        request=request,
        template_name='administrator/services/services.html',
        context={'services': all_services},
    )


def create_services(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='administrator/services/create_service.html',
        context={'segment': 'services'},
    )


def customers(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='administrator/home/customers.html',
        context={'segment': 'services'},
    )


def create_customers(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='administrator/home/create_customer.html',
        context={'segment': 'services'},
    )


def charges(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='administrator/home/charges.html',
        context={'segment': 'services'},
    )


def create_charge(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='administrator/home/create_charge.html',
        context={'segment': 'services'},
    )
