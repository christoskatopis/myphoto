from django.contrib import admin
from django.contrib.auth.models import User,Group
from django import forms 
from django.contrib.auth.forms import UserChangeForm
from .models import AccessAttempt


class AccessAdmin (admin.ModelAdmin):
  list_display = ["user_ip","attempt_time","login_attempts","blocked"]
  search_fields=["user_ip","attempt_time"]
  list_editable=["blocked"]
  list_filter=["blocked"]
class Meta:
     model = AccessAttempt


class UserAdmin(admin.ModelAdmin):
 list_display=["username","email","first_name","last_name","is_staff","is_superuser","is_active","last_login"]
 search_fields=["username"]
 list_filter=["is_staff","is_superuser","is_active"]
 list_editable=["is_active"]
 can_change=False


 class Meta:
    model=User


class UserChangeForm(forms.ModelForm): 
 class Meta:
    model=User
    fields=["username"]




 
 


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(AccessAttempt,AccessAdmin)