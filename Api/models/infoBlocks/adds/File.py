from django.db import models
from rest_framework import serializers

from UserFiles import path
from .. import FilesBlock


class File(models.Model):
    file = models.FileField(upload_to=path)

    position = models.PositiveSmallIntegerField()
    block = models.ForeignKey(FilesBlock, on_delete=models.CASCADE)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'file',
            'position',
            'block',
        ]