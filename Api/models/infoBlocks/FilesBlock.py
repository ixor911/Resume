from django.db import models
from rest_framework import serializers

from .. import Resume


types = {
    "image": "Images",
    "file": "Files",
    "pdf": "PDF",
    "presentation": "Presentation",
    "video": "Video"
}


class FilesBlock(models.Model):
    type = models.CharField(choices=types)
    status = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class FilesBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesBlock
        fields = [
            'type',
            'status',
            'position',
            'resume'
        ]