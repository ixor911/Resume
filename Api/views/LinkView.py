from django.views import View
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, status
from rest_framework.decorators import api_view

from Api.models import Link, LinkSerializer
from django.core.exceptions import ObjectDoesNotExist

class LinkView(View):
    @staticmethod
    @api_view(['GET'])
    def get(request, pk):
        try:
            link = Link.objects.get(id=pk)
            serializer = LinkSerializer(link)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    @api_view(['POST'])
    def post(request):
        serializer = LinkSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['PUT'])
    def put(request, pk):
        try:
            link = Link.objects.get(id=pk)
            serializer = LinkSerializer(link, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request, pk):
        try:
            link = Link.objects.get(id=pk)
            link.delete()
            Response(NotFound, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)