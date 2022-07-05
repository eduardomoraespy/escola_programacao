from django.shortcuts import render


def home(request):

    return render(
        request,
        'home.html'
    )


def form_base(request):

    return render(
        request,
        'componentes/form_base.html'
    )