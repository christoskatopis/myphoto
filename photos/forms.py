from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Photo,Comment
from django.contrib.auth.models import User

class PhotoForm(forms.ModelForm):
	class Meta:
	   model=Photo
	   fields= ["title","price","image","categories"]


class CommentForm(forms.ModelForm):
	class Meta:
	 model=Comment
	 fields=["text"]

