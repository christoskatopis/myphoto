from django.conf import settings
from django.utils import timezone
from django.contrib.auth.views import login
from django.shortcuts import render
from django.http import HttpResponseRedirect,QueryDict
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.template import loader
from django.utils.encoding import force_bytes
from .models import AccessAttempt
from .forms import UserForm

def is_logged_in(function):
 def wrap(request):
   user=request.user
   if user.is_authenticated()==True:
     return HttpResponseRedirect('/')
   else:
     return function(request)
 wrap.__doc__=function.__doc__
 wrap.__name__=function.__name__
 return wrap


def check_ip(request):
 x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
 if x_forwarded_for:
   ip = x_forwarded_for.split(',')[0]
 else:
   ip = request.META.get('REMOTE_ADDR')
 return ip


@is_logged_in
def is_locked_out(request):
   if request.method=="POST":
     ip = check_ip(request)
     userlocked,created=AccessAttempt.objects.get_or_create(user_ip=ip)
     if created:
       return login(request)
     else:
       blocked=userlocked.blocked
       if blocked:
         context={"blocked":blocked,"time":""}
         return render(request,"registration/login_failed.html",context)
       else:
         if userlocked.login_attempts > 3:
           now=timezone.now()
           time_passed= int ( (now - userlocked.attempt_time).total_seconds() )
           if time_passed < settings.LOCKOUT_TIME:
             time= settings.LOCKOUT_TIME - time_passed
             context={"blocked":blocked,"time":time}
             return render(request,"registration/login_failed.html",context)
           else:
             userlocked.delete()
             return login(request)
         else:
           userlocked.login_attempts=userlocked.login_attempts + 1
           userlocked.attempt_time=timezone.now()
           userlocked.save()
           return login(request)
   else:
     return login(request)

@is_logged_in
def create_account(request):
 form=UserForm(request.POST or None)
 if form.is_valid():
    user = form.save(commit=False)
    user.is_active=False
    user.save()
    token_generator=default_token_generator
    domain=get_current_site(request).domain
    if request.is_secure():
      protocol="https"
    else:
      protocol="http"
    context = {
       'domain': domain,
       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
       'token': token_generator.make_token(user),
       'protocol':protocol,
         }
    subject="my photo account activation"
    email=loader.render_to_string("registration/activation_email.html",context)
    send_mail(subject,email,"myphoto.team@gmail.com",[user.email])
    return HttpResponseRedirect("/accounts/activation")
 return render(request,"create_account.html",{"form":form})


def activation_confirm(request,uidb64=None, token=None):  
  token_generator=default_token_generator
  assert uidb64 is not None and token is not None  
  try:
   uid = force_text(urlsafe_base64_decode(uidb64))
   user = User.objects.get(pk=uid)
  except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
   user = None
  if user is not None and token_generator.check_token(user, token):
   validlink = True
   date = timezone.now()
   days_passed = (date - user.date_joined).days
   if (days_passed < settings.ACCOUNT_ACTIVATION_DAYS):
     context= {
         'validlink':validlink,
         'error_message':''
     }
     user.is_active=True
     user.save()
   else:
     validlink=False
     context = {
       'validlink': validlink,
       'error_message':'Your account has expired. Please create a new one.'
      }
  else:
   validlink = False
   context = {
     'validlink': validlink,
     'error_message':'The link is not valid. Please try again or create a new account.'
    }
  return render(request,"registration/activation_confirm.html",context)
    

