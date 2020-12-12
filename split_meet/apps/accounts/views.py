from django.shortcuts import render


def signup_user(request):
    context = {}
    return render(request, 'signup_page.html', context)


def login_user(request):
    context = {}
    return render(request, 'leaves/employee_leaves.html', context)


def logout_view(request):
    context = {}
    return render(request, 'leaves/employee_leaves.html', context)


def home(request):
    context = {}
    return render(request, 'signup_page.html', context)