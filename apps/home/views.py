from django.shortcuts import render, redirect


def view_home(request):

    context = {}

    return render(request, 'home/home.html', context)