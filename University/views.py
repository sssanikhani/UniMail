from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ClassSerializer


class CreateClassView(APIView):

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        response = ClassSerializer(obj).data
        return Response(response, status=status.HTTP_201_CREATED)
