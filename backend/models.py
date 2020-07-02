from django.db import models
# Create your models here.

class ZipCode(models.Model):
    zip_code = models.TextField()

    def __str__(self):
        return self.zip_code


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

    def __str__(self):
        return self.practice_name


class OldData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    id_1 = models.CharField(max_length=100)
    company_name = models.TextField(null=True, blank=True)
    duplicate = models.CharField(max_length=10, null=True, blank=True)
    shipping_address_1 = models.TextField(null=True, blank=True)
    shipping_address_2 = models.TextField(null=True, blank=True)
    shipping_city = models.TextField(null=True, blank=True)
    shipping_state = models.TextField(null=True, blank=True)
    shipping_zip = models.TextField(null=True, blank=True)
    shipping_country = models.TextField(null=True, blank=True)
    medical_license_number = models.TextField(null=True, blank=True)
    date_created = models.TextField(null=True, blank=True)
    sales_rep = models.TextField(null=True, blank=True)
    inactive = models.CharField(max_length=10, null=True, blank=True)
    secondary_sales_rep = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.id_1 + " | " + self.company_name

