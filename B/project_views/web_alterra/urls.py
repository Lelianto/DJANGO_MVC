from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('mentor', views.mentor, name='mentor'),
    path('mentee', views.mentee, name='mentee'),
    path('author', views.author, name='author')
]



