from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trainer/<int:trainer_id>/", views.trainer, name="trainer"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon")
    
]
