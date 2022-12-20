from django.db import models

# Create your models here.
class patient_details(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    date = models.DateField()
    room = models.IntegerField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
        