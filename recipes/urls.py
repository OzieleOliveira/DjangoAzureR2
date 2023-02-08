from sys import path_hooks
from django.urls import path
#from recipes.views import home, sobre, contato
from recipes.views import vai, home, contato
from . import views

# HTTP Request
urlpatterns = [
    path('', views.home),
    path('recipe/<int:id>/', views.recipe),
    path('vai/', vai, name='vai'),
    path('home/', home, name='home'),
    path('contato/', contato, name='contato'),
]
