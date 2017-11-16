from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import create_account,activation_confirm,is_locked_out
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required



urlpatterns=[
 url(r'^create/',create_account,name="create_account"),
 url(r'^activation/$',TemplateView.as_view(template_name="registration/activation.html")),
 url(r'^activation/(?P<uidb64>[0-9A-za-z]+)-(?P<token>.+)/',activation_confirm,name="activation"),
 url(r'^loggedout/',TemplateView.as_view(template_name="registration/loggedout.html")),
 url(r'^login/',is_locked_out,name="login"),
 url(r'^logout/',login_required(auth_views.logout,redirect_field_name=None),name="logout"),
 url(r'^password/reset/$',auth_views.password_reset,{"post_reset_redirect":"/accounts/password/reset/done"},name="password_reset"),
 url(r'^password/reset/done/$',auth_views.password_reset_done),
 url(r'^password/reset/(?P<uidb64>[0-9A-za-z]+)-(?P<token>.+)/$',auth_views.password_reset_confirm,{"post_reset_redirect":"/accounts/password/done"},name="password_reset_confirm"),
 url(r'^password/done/$',auth_views.password_reset_complete)
]