from django.db import models



class Image(models.Model):
    name = models.CharField(max_length=30)  # Add a name field with max length of 30 characters
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    


class UserData(models.Model):
    name = models.CharField(max_length=30,default='sexy')
    email = models.EmailField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
