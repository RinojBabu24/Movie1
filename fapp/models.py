from django.db import models


class Movie(models.Model):
    Name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='img')
    Year=models.IntegerField()
    Description=models.TextField()

    def __str__(self):  
        return self.Name


    


# Create your models here.
