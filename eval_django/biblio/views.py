from django.shortcuts import render
from django.shortcuts import HttpResponse
from biblio.models import Livres

def home(request):
	return render(request, 'biblio/accueil.html', locals())

def description(request, id_livres):
	livres = Livres.objects.get(id=id_livres)
	return render(request, 'biblio/description.html', {'livres': livres})
# Create your views here.
