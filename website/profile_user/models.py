from django.db import models

# Create your models here.
class user_details(models.Model):
    first_name = models.CharField(max_length=250,null=False, blank=False,default="")
    last_name = models.CharField(max_length=250, null=False, blank=False,default="")
    email_id = models.CharField(max_length=500, null=False, blank=False,default="")
    DateofBirth = models.DateField(null=True, blank=False)
    password = models.CharField(max_length=250, null=False, blank=False,default="")
    gender=models.CharField(max_length=10,null=False,blank=False,default="")
    address=models.CharField(max_length=100,null=False,blank=False,default="")
    city=models.CharField(max_length=100,null=False,blank=False,default="")
    state=models.CharField(max_length=100,null=False,blank=False,default="")
    zip=models.CharField(max_length=25,null=False,blank=False,default="")
    phonen=models.CharField(max_length=20,null=False,blank=False,default="")

    blood_group = models.CharField(max_length=10, null=False, blank=False, default="")
    drug_allergy =  models.NullBooleanField(default=False)
    addict_hist = models.NullBooleanField(default=False)
    psych_ill =  models.NullBooleanField(default=False)
    hypertension = models.NullBooleanField(default=False)
    diabetes=  models.NullBooleanField(default=False)
    asthma = models.NullBooleanField(default=False)
    bronchites=  models.NullBooleanField(default=False)
    fits =  models.NullBooleanField(default=False)
    any_congential=models.NullBooleanField(default=False)
    surgery_accident =  models.CharField(max_length=25, null=False, blank=False, default="")
    drug_intake = models.NullBooleanField(default=False)
    other = models.CharField(max_length=200, null=False, blank=False, default="")


    def __str__(self):
        return self.first_name
