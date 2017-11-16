from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
 class Meta:
	 model=User 
	 fields= {
	      "username",
	      "email",
	      "first_name",
	      "last_name"
	 }
	  
 def __init__(self, *args, **kwargs):
     super(UserForm,self).__init__(*args, **kwargs)
     self.fields['email'].required = True