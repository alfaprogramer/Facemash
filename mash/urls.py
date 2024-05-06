from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('facemash/', views.facemash, name="facemash"),
    path('facemash/next_pair/', views.facemash_next_pair, name='facemash_next_pair'),
    




    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
