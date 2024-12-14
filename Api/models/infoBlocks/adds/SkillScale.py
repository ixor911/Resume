from django.db import models
from .. import ObjectsBlock
from ... import Skill

class SkillScale(models.Model):
    experience = models.PositiveSmallIntegerField(blank=True)

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)
