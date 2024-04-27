from django.shortcuts import render
from random import sample
from .models import Image


def index(request):
    return render(request,'mash/index.html')


def facemash(request):
    # Get all images from the database
    all_images = Image.objects.all()
    
    # Sample two random images
    random_images = sample(list(all_images), 2)
    
    # Ensure that both images are different
    if random_images[0] == random_images[1]:
        random_images = sample(list(all_images), 2)
    
    context = {
        'image1': random_images[0],
        'image2': random_images[1]
    }
    
    return render(request, 'mash/facemash.html', context)


# Create your views here.
