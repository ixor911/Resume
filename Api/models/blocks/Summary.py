from django.db import models
from rest_framework import serializers

from .. import Block


class Summary(Block):
    text = models.TextField(blank=True)


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'