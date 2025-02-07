from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Api.models import Skill, SkillSerializer
from . import methods


@api_view(['GET'])
def get_all(request):
    data = methods.get_all()
    return Response(data)

@api_view(['POST'])
def create(request):
    try:
        data = methods.create(request.data)
        return Response(data, status=status.HTTP_201_CREATED)

    except Exception as err:
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def details_get(request, pk):
    try:
        data = methods.get(pk)
        return Response(data, status=status.HTTP_200_OK)

    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def details_put(request, pk):
    try:
        data = methods.update(pk, request.data)
        return Response(data, status=status.HTTP_200_OK)

    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    except Exception as err:
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def details_delete(request, pk):
    try:
        data = methods.delete(pk)
        return Response(data, status=status.HTTP_200_OK)

    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def details(request, pk):
    if request.method == "GET":
        return details_delete(request, pk)
    elif request.method == "PUT":
        return details_put(request, pk)
    elif request.method == "DELETE":
        return details_delete(request, pk)


