from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.SlugField(unique=True)
    phone_number = models.SlugField(unique=True)
    country = models.SlugField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.full_name
