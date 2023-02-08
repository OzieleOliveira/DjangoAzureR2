from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
# Create your views here.

# HTTP Request
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)], 'name': 'Burguer',
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(), 'name': 'Burguer',
        'is_detail_page' : True,
    })

def vai(request):
    return render(request,'recipes/part/vai.html', context={'name': 'Burguer'})

def contato(request):
    return render(request,'recipes/part/contato.html', context={'name': 'Burguer'})
  
# def contato(request):
#     # HTTP Response
#     return HttpResponse('')
