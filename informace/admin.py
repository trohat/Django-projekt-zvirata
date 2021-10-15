from django.contrib import admin
from .models import Zvire

# Register your models here.

class ZvireAdmin(admin.ModelAdmin):
    list_display = ("id", "jmeno", "vaha", "barva", "zije")
    list_filter = ("jmeno", "zije")

admin.site.register(Zvire, ZvireAdmin)
