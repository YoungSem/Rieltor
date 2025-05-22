from django.db import models

class Jk(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
