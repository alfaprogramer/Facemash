from django.db import models


class Image1(models.Model):
    sequence_number = models.IntegerField(default=1)  # Set default value to 1
    image1 = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image1 {self.sequence_number}"

class Image2(models.Model):
    sequence_number = models.IntegerField(default=1)  # Set default value to 1
    image2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image2 {self.sequence_number}"
   
