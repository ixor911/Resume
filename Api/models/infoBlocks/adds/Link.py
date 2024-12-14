from django.db import models
from .. import ObjectsBlock

class Link(models.Model):
    label = models.CharField(max_length=50, blank=True)
    link = models.CharField()

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)
