from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Class
from .serializers import ClassSerializer, StudentSerializer


class CreateClassView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        response = ClassSerializer(obj).data
        return Response(response, status=status.HTTP_201_CREATED)


class ClassView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, class_id):
        try:
            obj = Class.objects.get(pk=class_id)
        except Class.DoesNotExist:
            raise NotFound("class with this id does not exist")
        response = ClassSerializer(obj).data
        return Response(response)

    def delete(self, request, class_id):
        try:
            obj = Class.objects.get(pk=class_id)
        except Class.DoesNotExist:
            raise PermissionDenied()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, class_id):
        try:
            obj = Class.objects.get(pk=class_id)
        except Class.DoesNotExist:
            raise PermissionDenied()
        serializer = ClassSerializer(instance=obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        response = ClassSerializer(obj).data
        return Response(response)


class CreateStudentView(APIView):

    def post(self, request):
        many = type(request.data) is list
        serializer = StudentSerializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        objs = serializer.save()
        response = StudentSerializer(objs, many=many).data
        return Response(response, status=status.HTTP_201_CREATED)
