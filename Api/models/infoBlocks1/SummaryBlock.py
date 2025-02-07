from django.db import models
from rest_framework import serializers

from .. import Resume


class SummaryBlock(models.Model):
    text = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class SummaryBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryBlock
        fields = '__all__'