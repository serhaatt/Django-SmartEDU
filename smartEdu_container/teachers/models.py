from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500,blank=True)
    image = models.ImageField(upload_to="teachers/%Y/%m/%d/")
    facebook = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100,blank=True)
    linkedin = models.URLField(max_length=100,blank=True)
    youtube = models.URLField(max_length=100,blank=True)

    def __str__(self):
        return self.name

