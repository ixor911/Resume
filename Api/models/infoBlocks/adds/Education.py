from django.db import models
from rest_framework import serializers

from .. import ObjectsBlock
from ... import Skill


class Education(models.Model):
    school = models.CharField(max_length=50, blank=True)
    degree = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    is_now = models.BooleanField(default=False)

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)

    skills = models.ManyToManyField(Skill, blank=True)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'school',
            'degree',
            'city',
            'description',
            'start_date',
            'end_date',
            'is_now',
            'position',
            'block',
            'skills',
        ]