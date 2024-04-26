from django.contrib import admin
from .models import Image1, Image2

@admin.register(Image1)
class Image1Admin(admin.ModelAdmin):
    list_display = ['id', 'image1']

@admin.register(Image2)
class Image2Admin(admin.ModelAdmin):
    list_display = ['id', 'image2']