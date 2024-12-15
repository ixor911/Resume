from django.db import models
from rest_framework import serializers

from .. import Resume


types = {
    'education': "Education",
    'language': "Languages",
    'link': "Links",
    'experience': "Professional experience",
    'skill': "Skills"
}


class ObjectsBlock(models.Model):
    type = models.CharField(choices=types)
    status = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class ObjectsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectsBlock
        fields = [
            'type',
            'status',
            'position',
            'resume'
        ]