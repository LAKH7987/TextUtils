
from django.contrib import admin
from django.urls import path
from . import views

# Code for video 7
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('youtube', views.youtube, name='youtube'),
    path('contact', views.contact, name='contact')

]
