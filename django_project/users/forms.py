from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()
  
  # specify the type of model we want our Form to interact with:
  class Meta:
    model = User
    
    # The fields we want available for this form
    # password 1 and 2 are the initial and confirmation password
    fields = ['username', 'email', 'password1', 'password2']