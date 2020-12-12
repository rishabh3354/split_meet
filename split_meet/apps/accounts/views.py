from django.shortcuts import render


def signup_user(request):
    context = {}
    return render(request, 'index_sign_up.html', context)


def login_user(request):
    context = {}
    return render(request, 'leaves/employee_leaves.html', context)


def logout_view(request):
    context = {}
    return render(request, 'leaves/employee_leaves.html', context)


def home(request):
    context = {}
    return render(request, 'index.html', context)