from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from django.shortcuts import redirect
from .forms import FilmForm

def index(request):
    film_list = Film.objects.all()

    context = {
        'film_list': film_list,
    }
    return render (request, 'films/index.html', context)

def details(request, film_id):
    film = Film.objects.get(pk=film_id)

    context = {
        'film': film,
    }

    return render(request, 'films/detail.html', context)

def new_film(request):
    form = FilmForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('films:index')
    
    return render(request, 'films/film_form.html', {'form': form})

def edit_film(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect('films:index')
    
    return render(request, 'films/film_form.html', {'form': form, 'film': film})

def delete_film(request, id):
    film = Film.objects.get(id=id)
    if request.method == 'POST':
        film.delete()
        return redirect('films:index')

    return render(request, 'films/delete_film.html',{'film':film})