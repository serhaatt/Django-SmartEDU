from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    phone = models.CharField(max_length=11,blank=False)
    message = models.TextField(max_length=300,blank=True)

    def __str__(self):
        return self.email

