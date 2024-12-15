from django.db import models
from rest_framework import serializers

from .. import ObjectsBlock
from ... import Language


class LanguageScale(models.Model):
    experience = models.PositiveSmallIntegerField(blank=True)

    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)


class LanguageScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageScale
        fields = [
            'experience',
            'language',
            'position',
            'block',
        ]
