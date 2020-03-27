from django.shortcuts import render, redirect
from assets.models import AssetsInfo


def view_home(request):
    assets_infos = AssetsInfo.objects.all().order_by('dividende', 'variation').reverse()

    context = {'assets_infos': assets_infos}

    return render(request, 'home/home.html', context)
