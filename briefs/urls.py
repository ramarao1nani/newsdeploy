from django.urls import path
from . import views

app_name='briefs'
urlpatterns = [
    path('', views.home,name='home'),
    path('india', views.india,name='india'),
    path('technology', views.technology,name='technology'),
    path('business', views.business,name='business'),
    path('world', views.world,name='world')
]