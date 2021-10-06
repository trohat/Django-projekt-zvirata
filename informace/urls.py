from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:zvire>", views.zvire_podle_cisla),
    path("<str:zvire>", views.info_o_zvireti, 
                name="zvire_info"),
]

# path converter - int, str, slug, uuid, path