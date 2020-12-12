from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^signup_user/$', views.signup_user, name="signup_user"),
    url(r'^login_user/$', views.login_user, name="login_user"),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'', views.home, name='home'),
]