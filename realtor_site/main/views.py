from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Jk, House, Flat, Application
from .forms import ApplicationForm

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

def flat_detail(request, flat_id):
    flat = get_object_or_404(Flat, id=flat_id)
    return render(request, 'flat_detail.html', {'flat': flat})

def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            if not application.flat:  # Если квартира не выбрана
                application.flat = None
            application.save()
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('welcome')
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form})