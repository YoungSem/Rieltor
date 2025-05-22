from django.shortcuts import render
from .models import Jk

def welcome(request):
    jk_list = Jk.objects.all()
    return render(request, 'welcome.html', {'jk_list': jk_list})