from django.db import models
from rest_framework import serializers


class Skill(models.Model):
    name = models.CharField(max_length=100)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'name'
        ]