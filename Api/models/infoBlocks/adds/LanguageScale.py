from django.db import models
from .. import ObjectsBlock
from ... import Language

class LanguageScale(models.Model):
    experience = models.PositiveSmallIntegerField(blank=True)

    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)
