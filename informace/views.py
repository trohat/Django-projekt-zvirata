from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

zvirata = {
    "krtek" : "krtek žije pod zemí",
    "hroch" : "hroch má hroší kůži",
    "krokodyl" : "krokodýl má hodně zubů",
    "slon" : "slon má kly - už nic jiného než slovník není",
    "zirafa": "žirafa má dlouhý krk"
}

def index(request):
    return HttpResponse("moje první stránka v Djangu")

def info_o_zvireti(request, zvire):
    try:
        cislo = list(zvirata.keys()).index(zvire) + 1
        response = f"<h1>Informace: {zvirata[zvire]}</h1><h2>a má číslo {cislo} </h2>"
        return HttpResponse(response)
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