from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .models import Zvire
from .forms import ZvireForm

# Create your views here.

class VypisZvirataView(ListView):
    model = Zvire
    template_name = "informace/index.html"
    context_object_name = "zvirata"

# def index(request):
#     zvirata = Zvire.objects.all()[:3]
#     return render(request, "informace/index.html", {
#         "zvirata": zvirata
#     })


class InfoOZvireti(DetailView):
    model = Zvire
    template_name = "informace/info.html"
    # context_object_name = "zvire"

# def info_o_zvireti(request, jmeno):
#     #try:
#     #    zvire = Zvire.objects.get(jmeno=jmeno)
#     #except:
#     #    raise Http404()
#     zvire = get_object_or_404(Zvire, jmeno=jmeno)
#     return render(request, "informace/info.html", {
#         "zvire": zvire
#     })


class NoveZvire3View(CreateView):
    form_class = ZvireForm
    template_name = "informace/nove.html"
    success_url = "dekuji"

class NoveZvire2View(FormView):
    form_class = ZvireForm
    template_name = "informace/nove.html"
    success_url = "dekuji"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class NoveZvireView(View):
    def get(self, request):
        formular = ZvireForm()
        return render(request, "informace/nove.html", {
            "formular": formular
        })

    def post(self, request):
        formular = ZvireForm(request.POST)
        if formular.is_valid():
            formular.save()
            return HttpResponseRedirect("dekuji")
        return render(request, "informace/nove.html", {
                "formular": formular
        })

# def nove_zvire(request):
#     if request.method == "POST":
#         formular = ZvireForm(request.POST)
#         if formular.is_valid():
#             formular.save()
#             return HttpResponseRedirect("dekuji")
#     else:
#         formular = ZvireForm()
#     return render(request, "informace/nove.html", {
#         "formular": formular
#     })


class DekujiView(TemplateView):
    template_name = "informace/dekuji.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["zprava"] = "ahoj tohle je zpráva"
        return context

# def dekuji(request):
#     return render(request, "informace/dekuji.html")


#view funkce

#view třídy