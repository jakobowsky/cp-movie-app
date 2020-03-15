from django.shortcuts import render, redirect
from .models import Movie


def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_result': search_result}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend) 

def create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            print(request.POST)
            response = Movie.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                rating=data.get('rating'),
                notes=data.get('notes'),

            )
        except Exception as e:
            pass
    return redirect('/')


def edit(request, movie_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            movie_obj = Movie.objects.get(id=movie_id)
            movie_obj.name = data.get('name')
            movie_obj.picture = data.get('picture')
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            movie_obj.save()        
        except Exception as e:
            pass
        return redirect('/')

def delete(request, movie_id):
    try:
        movie_obj = Movie.objects.get(id=movie_id)
        movie_name = movie_obj.name
        movie_obj.delete()
    except Exception as e:
        pass
    return redirect('/')