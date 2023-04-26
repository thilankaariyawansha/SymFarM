from django.db import models

# Create your models here.

class machines(models.Model): 
    tag=models.CharField(max_length=200) 
    mid = models.CharField(max_length=200) 
    img = models.ImageField()
    date_time = models.DateTimeField(auto_now=True)
    
    
    registration_number = models.CharField(max_length=200)
    machine_type = models.CharField(max_length=200)
    mark = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    date_of_purches = models.DateField()
    year_of_manufacture = models.CharField(max_length=200)
    country_of_origine = models.CharField(max_length=200)
    cost = models.IntegerField()
    owner = models.CharField(max_length=200)
    owner_contact=models.CharField(max_length=200)
    
    def __str__(self):
        return self.mid
