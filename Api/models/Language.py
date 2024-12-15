from django.db import models
from rest_framework import serializers


class Language(models.Model):
    name = models.CharField(max_length=50)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'name'
        ]
