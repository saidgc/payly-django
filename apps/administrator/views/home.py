from django.shortcuts import redirect, render


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

    return render(
        request=request,
        template_name='administrator/home/services.html',
        context={'segment': 'services'},
    )
