from django.db import models


class Diseases_Symptoms(models.Model):
    disease = models.CharField(max_length=100)
    symptom1 = models.CharField(max_length=250)
    symptom2 = models.CharField(max_length=250)
    symptom3 = models.CharField(max_length=250)
    symptom4 = models.CharField(max_length=250)
    symptom5 = models.CharField(max_length=250)
    symptom6 = models.CharField(max_length=250)
    age_group=models.CharField((
        ('Newborn (0-28 days)'),
        ('Infant (29 days-1 year)'),
        ('Younger Child (1 year-5 years)'),
        ('Older Child (6-12 years)'),
        ('Adolescent (13-16 years)'),
        ('Young Adult (17-29 years)'),
        ('Adult (30-39 years)'),
        ('Adult (40-49 years)'),
        ('Adult (50-64 years)'),
        ('Senior (65 years-over)')), max_length=250, default="choose any age group")
    gender=models.CharField((
        ('Male'),
        ('Female')), default="none",max_length=10)
    is_pregnant=models.BooleanField(default=False)

    def __str__(self):
        return self.disease

