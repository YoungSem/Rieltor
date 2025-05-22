from django.db import models
from django.contrib.auth.models import User

class Jk(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jks', null=True)

    def __str__(self):
        return self.name

class House(models.Model):
    adres = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    description = models.TextField()
    jk = models.ForeignKey(Jk, on_delete=models.CASCADE, related_name='houses')
    floors = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='houses')

    def __str__(self):
        return self.adres

class Flat(models.Model):
    number = models.CharField(max_length=50)
    area = models.CharField(max_length=255)
    description = models.TextField()
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='flats')
    floor = models.IntegerField()
    rooms = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flats')

    def __str__(self):
        return f"{self.house}: {self.number}"

class Jk_media(models.Model):
    path = models.CharField(max_length=255)
    jk = models.ForeignKey(Jk, on_delete=models.CASCADE, related_name='media')

class House_media(models.Model):
    path = models.CharField(max_length=255)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='media')

class Flat_media(models.Model):
    path = models.CharField(max_length=255)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='media')

class Application(models.Model):
    person_name = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=50)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='applications')