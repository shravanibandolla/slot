from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('available/', views.available_slots, name="available_slots"),
    path('booked/', views.booked_slots, name="booked_slots"),
    path('book/<int:id>/', views.book_slot, name="book_slot"),
    path('add/', views.add_slot, name="add_slot"),
]