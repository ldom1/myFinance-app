from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.apps import apps
import numpy as np
from django.contrib.auth.models import User

from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    # Form to get data
    template_name = 'users/profile.html'

    context = {'user': request.user.get_username()}

    return render(request, template_name, context)
