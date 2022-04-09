from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html',	{'searchTerm':searchTerm, 'movies': movies})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})
