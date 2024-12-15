from django.db import models
from rest_framework import serializers

from .. import ObjectsBlock


class Link(models.Model):
    label = models.CharField(max_length=50, blank=True)
    link = models.CharField()

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            'label',
            'link',
            'position',
            'block',
        ]