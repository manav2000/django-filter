from django.shortcuts import render
from .models import *
from .filters import FilmFilter


# Create your views here.

def film_list(request):
    films = Film.objects.all()
    filter = FilmFilter(request.GET, queryset=films)
    return render(request, 'app/index.html', {
        'filter': filter
    })
