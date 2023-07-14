from django.db import models


class Work(models.Model):
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.SlugField(unique=True)
    sector = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    country = models.SlugField(unique=True)
    city = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
