from django.urls import path
from . import views

app_name = 'web_alterra'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('mentor', views.mentor, name='mentor'),
    path('mentee', views.mentee, name='mentee'),
    path('author', views.author, name='author'),
    path('content_blog', views.content_blog, name='content_blog'),
    path('save_new_content', views.save_new_content, name='save_new_content')
]



