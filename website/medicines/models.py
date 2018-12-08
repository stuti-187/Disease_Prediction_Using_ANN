from django.db import models

# Create your models here.
class medicinedata1(models.Model):
    name = models.CharField(max_length=250,null=False, blank=False,default="")
   # composition = models.CharField(max_length=250, null=False, blank=False,default="")
    price = models.CharField(max_length=500, null=False, blank=False,default="")
    category = models.CharField(null=True, blank=False,max_length=250,default="")
    quantity = models.CharField(max_length=250, null=False, blank=False,default="")

    def __str__(self):
        return self.name
