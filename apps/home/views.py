from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView


def view_home(request):

    context = {}

    return render(request, 'home/home.html', context)