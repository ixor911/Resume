from django.db import models
from ..Resume import Resume


class InfoBlock(models.Model):
    status = models.BooleanField(default=False)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)