from django.contrib import admin
from .models import Image, UserData

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']



@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    def name(self, obj):
        return obj.image.name

    name.short_description = 'Image Name'
