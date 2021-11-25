from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nove_zvire", views.nove_zvire, name="nove_zvire"),
    path("dekuji", views.dekuji, name="dekuji"),
    path("<str:jmeno>", views.info_o_zvireti, name="zvire_info")
]

# path converter - int, str, slug, uuid, path