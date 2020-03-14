from django.urls import path
from .views import home_page, create


urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
]
