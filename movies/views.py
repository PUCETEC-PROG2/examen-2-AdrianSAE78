from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movies

# Create your views here.

def index(request):
    movies = Movies.objects.order_by('genre')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def details(request, movie_id):
    movie = Movies.objects.get(id = movie_id)
    template = loader.get_template('details.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))
    