from django.shortcuts import render


def index(request):
    return render(request,'mash/index.html')


def facemash(request):
    return render(request,'mash/facemash.html')


# Create your views here.
