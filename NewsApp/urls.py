from django.urls import path
from .views import About, Home, News
urlpatterns = [
    path('',Home,name = 'home'),
    path('news/', News, name='home'),
    path('about/', About, name='home')

]