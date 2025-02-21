from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, status

from Api.models import Resume, ResumeSerializer
from django.core.exceptions import ObjectDoesNotExist


class ResumeView(APIView):
    def get(self, request, pk):
        try:
            resume = Resume.objects.get(id=pk)
            serializer = ResumeSerializer(resume)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)

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
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)