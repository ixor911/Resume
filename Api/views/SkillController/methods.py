from Api.models import Skill, SkillSerializer


def get_all():
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return serializer.data

def get(pk: int):
    skill = Skill.objects.get(pk=pk)
    serializer = SkillSerializer(skill)
    return serializer.data

def create(data: dict):
    serializer = SkillSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data

    raise serializer.errors

def update(pk: int, data: dict):
    skill = Skill.objects.get(pk=pk)
    serializer = SkillSerializer(skill, data=data)

    if serializer.is_valid():
        serializer.save()
        return serializer.data

    raise serializer.errors

def delete(pk: int):
    skill = Skill.objects.get(pk=pk)
    skill.delete()