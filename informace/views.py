from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

zvirata = {
    "krtek" : "krtek žije pod zemí",
    "hroch" : "hroch má hroší kůži",
    "krokodyl" : "krokodýl má hodně zubů",
    "slon" : "slon má dlouhý chobot",
    "zirafa": "žirafa má dlouhý krk",
    "pes" : "pes je nejkrásnější zvíře na světě"
}

def index(request):
    return render(request, "informace/index.html", {
        "zvirata": zvirata
    })

def info_o_zvireti(request, zvire):
    try:
        cislo = list(zvirata.keys()).index(zvire) + 1
        return render(request, "informace/info.html", {
            "zvire_v_sablone": zvire,
            "informace": zvirata[zvire],
            "cislo": cislo
        })
    except:
        return HttpResponseNotFound(f"Zvíře {zvire} nebylo nalezeno.")

def zvire_podle_cisla(request, zvire):
    try:
        jmeno_zvirete = list(zvirata.keys())[zvire - 1]
        return HttpResponseRedirect(jmeno_zvirete)
    except:
        return HttpResponseNotFound("Zvíře s tímto číslem neexistuje.")

#view funkce

#view třídy