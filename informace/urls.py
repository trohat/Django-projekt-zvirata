from django.urls import path

from . import views

urlpatterns = [
    path("", views.VypisZvirataView.as_view(), name="index"),
    path("nove_zvire", views.NoveZvire3View.as_view(), name="nove_zvire"),
    path("dekuji", views.DekujiView.as_view(), name="dekuji"),
    path("<pk>", views.InfoOZvireti.as_view(), name="zvire_info")
]

# path converter - int, str, slug, uuid, path