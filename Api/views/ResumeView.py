from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, status

from Api.models import Resume, ResumeSerializer
from django.core.exceptions import ObjectDoesNotExist


class ResumeView(View):
    @api_view(['GET'])
    def get(self, request, pk):
        try:
            resume = Resume.objects.get(id=pk)
            serializer = ResumeSerializer(resume)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(NotFound, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def put(self, request, pk):
        try:
            resume = Resume.objects.get(id=pk)
            serializer = ResumeSerializer(resume, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(NotFound, status=status.HTTP_404_NOT_FOUND)