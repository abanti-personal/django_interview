from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.suite}, {self.city}, {self.zipcode}"


class Company(models.Model):
    name = models.CharField(max_length=255)
    catch_phrase = models.CharField(max_length=255)
    bs = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    website = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
