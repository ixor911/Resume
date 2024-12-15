from django.db import models
from rest_framework import serializers

from .. import ObjectsBlock
from ... import Skill, Language


class ProfessionalExperience(models.Model):
    job_title = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    is_now = models.BooleanField(default=False)

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(ObjectsBlock, on_delete=models.CASCADE)

    skills = models.ManyToManyField(Skill, blank=True)
    languages = models.ManyToManyField(Language, blank=True)


class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperience
        fields = [
            'job_title',
            'employer',
            'city',
            'description',
            'start_date',
            'end_date',
            'is_now',
            'position',
            'block',
            'skills',
            'languages',
        ]
