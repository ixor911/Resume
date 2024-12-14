from django.db import models
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