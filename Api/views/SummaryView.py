from django.views import View
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, status
from rest_framework.decorators import api_view

from Api.models import Summary, SummarySerializer
from django.core.exceptions import ObjectDoesNotExist

class SummaryView(View):
    @api_view(['GET'])
    def get(self, request, pk):
        try:
            summary = Summary.objects.get(id=pk)
            serializer = SummarySerializer(summary)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(NotFound, status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def post(self, request):
        serializer = SummarySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    @api_view(['PUT'])
    def put(self, request, pk):
        try:
            summary = Summary.objects.get(id=pk)
            serializer = SummarySerializer(summary, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(NotFound, status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def delete(self, request, pk):
        try:
            summary = Summary.objects.get(id=pk)
            summary.delete()
            Response(NotFound, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(NotFound, status=status.HTTP_404_NOT_FOUND)