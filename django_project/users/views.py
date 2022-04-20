from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
  if request.method == 'POST':
    # If delivered a post from the form, save the form data
    form = UserRegisterForm(request.POST)

    # Use builtin from FORM to check if the data is valid
    if form.is_valid():
      # save the form data, using the built-in function save()
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created! You are now able to log in! {username}!')

      return redirect('login')

  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
  return render(request, 'users/profile.html')