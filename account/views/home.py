from django.shortcuts import redirect, render


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {
        'title': 'Cuenta',
    }
    return render(
        request=request,
        template_name='account.html',
        context=context,
    )
