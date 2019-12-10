from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'web_alterra/home.html', {})
def blog(request):
    return render(request, 'web_alterra/blog.html', {})
def mentee(request):
    return render(request, 'web_alterra/mentee.html', {})
def mentor(request):
    return render(request, 'web_alterra/mentor.html', {})
def author(request):
    return render(request, 'web_alterra/author.html', {})



