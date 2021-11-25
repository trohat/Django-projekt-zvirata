from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Zvire
from .forms import ZvireForm

# Create your views here.

def index(request):
    zvirata = Zvire.objects.all()
    return render(request, "informace/index.html", {
        "zvirata": zvirata
    })

def info_o_zvireti(request, jmeno):
    #try:
    #    zvire = Zvire.objects.get(jmeno=jmeno)
    #except:
    #    raise Http404()
    zvire = get_object_or_404(Zvire, jmeno=jmeno)
    return render(request, "informace/info.html", {
        "jmeno": zvire.jmeno,
        "vaha" : zvire.vaha,
        "barva" : zvire.barva[:-1] + "ou",
        "zije": zvire.zije
    })

def nove_zvire(request):
    if request.method == "POST":
        formular = ZvireForm(request.POST)
        if formular.is_valid():
            #zde dochází ke zpracování dat
            # zvire = Zvire(jmeno=formular.cleaned_data["jmeno"],
            #             vaha=formular.cleaned_data["vaha"] + 10,
            #             barva=formular.cleaned_data["barva"],
            #             zije=formular.cleaned_data["zije"]
            #                 )
            formular.save()
            return HttpResponseRedirect("dekuji")
        
    else:
        formular = ZvireForm()
    return render(request, "informace/nove.html", {
        "formular": formular
    })

def dekuji(request):
    return render(request, "informace/dekuji.html")


#view funkce

#view třídy