from django.db.models import fields
from django.forms import ModelForm
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class contact_us_form(ModelForm):
    class Meta:
        model=contact_us_form
        fields='__all__'