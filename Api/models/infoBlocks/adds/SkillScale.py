from django.db import models
from rest_framework import serializers

from .. import ObjectsBlock
from ... import Skill


class SkillScale(models.Model):
    experience = models.PositiveSmallIntegerField(blank=True)

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)


class SkillScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillScale
        fields = [
            'experience',
            'skill',
            'position',
            'block',
        ]