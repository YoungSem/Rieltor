from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('jk/<int:jk_id>/houses/', views.houses_list, name='houses_list'),
    path('house/<int:house_id>/flats/', views.flats_list, name='flats_list'),
    path('flat/<int:flat_id>/', views.flat_detail, name='flat_detail'),
    path('application/create/', views.application_create, name='application_create'),
]