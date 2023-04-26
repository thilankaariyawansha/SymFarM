from django.db import models

# Create your models here.


class lands(models.Model): 
    tag=models.CharField(max_length=200)
    lid = models.CharField(max_length=200) 
    uidimg = models.ImageField()
    date_time = models.DateTimeField(auto_now=True)
     
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nic = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    
    lat = models.CharField(max_length=200)
    log = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    ownership = models.CharField(max_length=200)
    rf_ir = models.CharField(max_length=200)
    soil = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.lid
