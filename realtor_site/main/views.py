from django.shortcuts import render, get_object_or_404
from .models import Jk, House, Flat

def welcome(request):
    jk_list = Jk.objects.all()
    return render(request, 'welcome.html', {'jk_list': jk_list})

def houses_list(request, jk_id):
    jk = get_object_or_404(Jk, id=jk_id)
    houses = House.objects.filter(jk=jk)
    return render(request, 'houses_list.html', {
        'houses': houses,
        'jk': jk
    })

def flats_list(request, house_id):
    house = get_object_or_404(House, id=house_id)
    flats = Flat.objects.filter(house=house)
    return render(request, 'flats_list.html', {
        'flats': flats,
        'house': house
    })