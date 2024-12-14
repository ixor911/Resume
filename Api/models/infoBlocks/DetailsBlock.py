from django.db import models
from Api.models import Resume

class DetailsBlock(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    image = models.ImageField(max_length=50, blank=True)

    position = models.PositiveSmallIntegerField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
