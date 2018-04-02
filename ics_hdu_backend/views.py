from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def chairs(request):
    return render(request, 'chairs.html')


def conference(request):
    return render(request, 'conference.html')


def about(request):
    return render(request, 'about.html')
