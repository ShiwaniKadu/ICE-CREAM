from django.db import models
from django.contrib.auth.models import User

#makemigrations - create changes an store in a file
#migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
    
class IceCream(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    IceCream_name = models.CharField(max_length=100)
    IceCream_description = models.TextField()
    IceCream_image = models.ImageField(upload_to="ice-cream")
    IceCream_view_count = models.IntegerField(default=1)    
