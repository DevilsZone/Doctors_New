from django.db import models
from process_zipcode import download_data
# Create your models here.

class ZipCode(models.Model):
    zip_code = models.TextField()

    def __str__(self):
        return self.zip_code

    def save(self, *args, **kwargs):
        if self.id:
            super(ZipCode, self).save(*args, **kwargs)
        else:
            super(ZipCode, self).save(*args, **kwargs)
            doctors_data = download_data(self.zip_code)
            if doctors_data:
                for data in doctors_data:
                    DoctorData(practice_name=data['PracticeName'], first_name=data['FirstName'],
                               last_name=data['LastName'], address=data['Address'], city=data['City'],
                               state=data['State'], zip=data['Zip'], phone=data['Phone'], speciality=data['Specialty']
                               , lat=data['Latitude'], long=data['Longitude'], distance=data['Distance'],
                               doctors=data['Specialists'], relation_manager=self).save()


class DoctorData(models.Model):
    practice_name = models.TextField()
    first_name = models.TextField(max_length=100, null=True, blank=True)
    last_name = models.TextField(max_length=100, null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    phone = models.CharField(max_length=30, null=True, blank=True)
    speciality = models.CharField(max_length=100, null=True, blank=True)
    lat = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    doctors = models.TextField(null=True, blank=True)
    relation_manager = models.ForeignKey(ZipCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.practice_name + " | " + self.city

