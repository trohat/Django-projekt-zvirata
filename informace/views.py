from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, Http404


from .models import Zvire

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


#view funkce

#view třídy