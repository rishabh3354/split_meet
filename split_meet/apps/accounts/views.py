import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.accounts.helpers import email_validation_check


class SignupUser(View):

    def get(self, request):
        """
        :param request:
        :return:
        """
        context = {}
        return render(request, 'sign_up.html', context)

    def post(self, request):
        """
        :param request:
        :return:
        """
        try:
            signup_data = json.loads(request.body)
            if email_validation_check(signup_data.get("email")):
                pass
            else:
                return HttpResponse("Please provide valid email address", status=400)

        except Exception as odne:
            return HttpResponse("Matching query does not exist", status=400)


def login_user(request):
    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    context = {}
    return render(request, 'leaves/employee_leaves.html', context)


def home(request):
    context = {}
    return render(request, 'landing_page.html', context)
