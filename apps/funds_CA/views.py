from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.apps import apps
import numpy as np
from datetime import datetime

from .models import *


@login_required
def view_display_funds(request):

    funds = fundsCA.objects.all().order_by('id_fund', 'date')
    context = {'funds': funds}

    return render(request, 'funds_CA/display_funds.html', context)