from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:zvire>", views.zvire_podle_cisla),
    path("<str:zvire>", views.info_o_zvireti),
]

# path converter - int, str, slug, uuid, path