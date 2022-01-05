from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
from django.shortcuts import render
from .serializers import testSerializer
from .models import test
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def students_list_or_create(request):
    if request.method == "GET":
        students_qs = test.objects.all()
        student_serializers = testSerializer(students_qs, many=True)
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    else:
        student_serializers = testSerializer(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def students_get_or_update(request, pk):
    student = get_object_or_404(test, id=pk)
    if request.method == "GET":
        student_serializers = testSerializer(student)
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        student_serializers = testSerializer(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)
# Create your views here.
# def students_get_or_update():
#     return None