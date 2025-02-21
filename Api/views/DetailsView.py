from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, status

from Api.models import DetailsSerializer, Details
from django.core.exceptions import ObjectDoesNotExist


class DetailsView(APIView):
    def get(self, request, pk):
        try:
            details = Details.objects.get(id=pk)
            serializer = DetailsSerializer(details)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            details = Details.objects.get(id=pk)
            serializer = DetailsSerializer(details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            details = Details.objects.get(id=pk)
            details.delete()
            Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(NotFound.default_detail, status=status.HTTP_404_NOT_FOUND)