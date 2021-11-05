from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def home(request):
    return render(request, 'webapp/home.html')


def store(request):
    return render(request, 'webapp/store.html')


def forums(request):
    return render(request, 'webapp/forums.html')
