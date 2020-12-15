import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views import View
from apps.accounts.helpers import email_validation_check, check_if_password_match
from apps.accounts.models import User


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
            context = dict()
            context["response"] = "Something went wrong"
            signup_data = request.POST
            if email_validation_check(signup_data.get("email")):
                context["first_name"] = signup_data.get("first_name")
                context["last_name"] = signup_data.get("last_name")
                context["email"] = signup_data.get("email")
                context["password"] = signup_data.get("pass")
                context["re_pass"] = signup_data.get("re_pass")

                if check_if_password_match(context["password"], context["re_pass"]):
                    new_user = User.objects.create_user(username=context["email"], email=context["email"],
                                                        first_name=context["first_name"],
                                                        last_name=context["last_name"],
                                                        password=context["password"])
                    if new_user:
                        context["response"] = f"{new_user.email} Successfully registered with us."
                else:
                    context["response"] = "your password does not match!"
            else:
                context["response"] = "Enter valid email address!"
            return render(request, 'sign_up.html', context)

        except Exception as error:
            return render(request, 'sign_up.html', {"response": error})


def login_user(request):
    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    context = {}
    return render(request, 'leaves/employee_leaves.html', context)


def home(request):
    context = {}
    return render(request, 'landing_page.html', context)
