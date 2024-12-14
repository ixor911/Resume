from django.db import models
from Api.models import Resume

class SummaryBlock(models.Model):
    text = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
