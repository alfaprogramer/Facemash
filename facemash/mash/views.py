from django.shortcuts import render


def index(request):
    return render(request, 'mash\index.html')

# Create your views here.
