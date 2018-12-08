from django.db import models

# Create your models here.
class DoctorData(models.Model):
    name = models.CharField(max_length=500,null=False, blank=False,default="")
    type = models.CharField(max_length=250, null=False, blank=False,default="")
    hospital_name = models.CharField(max_length=500, null=False, blank=False,default="")
    monday = models.CharField(max_length=500,null=False, blank=False,default="")
    tuesday = models.CharField(max_length=500, null=False, blank=False, default="")
    wednesday = models.CharField(max_length=500, null=False, blank=False, default="")
    thursday = models.CharField(max_length=500, null=False, blank=False, default="")
    friday = models.CharField(max_length=500, null=False, blank=False, default="")
    saturday = models.CharField(max_length=500, null=False, blank=False, default="")
    sunday = models.CharField(max_length=500, null=False, blank=False, default="")

    def __str__(self):
        return self.name

class hospital(models.Model):
    name=models.CharField(max_length=500,null=False, blank=False,default="")
    address=models.CharField(max_length=500,null=False, blank=False,default="")
    city=models.CharField(max_length=500,null=False, blank=False,default="")
    state=models.CharField(max_length=500,null=False, blank=False,default="")
    zip=models.CharField(max_length=500,null=False, blank=False,default="")
    map_url=models.CharField(max_length=5000,null=False, blank=False,default="")
    def __str__(self):
        return self.name
