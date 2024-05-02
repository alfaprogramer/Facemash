from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from random import sample
from .models import Image,UserData



def index(request):
    return render(request,'mash/index.html')


def facemash(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        
        # Save data to database
        image_obj = Image.objects.create(name=name, image=image)
        UserData.objects.create(name=name, email=email, image=image_obj)
        
        # Redirect to a success page or render a success message
        # Here, I'm returning an HttpResponse with a success message
        return HttpResponse('<script>alert("Image added successfully!"); window.location.href = "http://127.0.0.1:8000/facemash";</script>')
    else:
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







def facemash_next_pair(request):
    # Get the IDs of previously selected images from session data or any other method
    previously_selected_ids = request.session.get('previously_selected_ids', [])

    # Retrieve all images from the database excluding the previously selected images
    all_images = Image.objects.exclude(id__in=previously_selected_ids)

    # Sample two random images
    random_images = sample(list(all_images), 2)

    # Prepare the response data
    data = {
        'image1_url': random_images[0].image.url,
        'image2_url': random_images[1].image.url,
        'image1_name': random_images[0].name,  # Include image name
        'image2_name': random_images[1].name,  # Include image name
        
    }

    # Store the IDs of the newly selected images in session data
    request.session['previously_selected_ids'] = [random_images[0].id, random_images[1].id]

    return JsonResponse(data)
# Create your views here.



