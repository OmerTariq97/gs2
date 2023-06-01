from django.shortcuts import render
from .serializers import StudentSerializer,CourseSerializer,InstructorSerializer,SingerSerializer,SongSerializer
from .models import Student,Course,Instructor,Singer,Song
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views import View
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from firebase_admin import firestore
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

# @method_decorator(csrf_exempt, name='dispatch')
# class StudentAPI(View):
#     def get(self, request, *args, **kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id',None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')

#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return JsonResponse(serializer.data,safe=False)

#     def post(self, request, *args, **kwargs):
#             json_data=request.body
#             stream=io.BytesIO(json_data)
#             python_data=JSONParser().parse(stream)
#             serializer=StudentSerializer(data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res={'msg':'Data_created'}
#                 return JsonResponse(res)
#             return JsonResponse(serializer.errors)

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Student registered')
        return Response(serializer.errors)
    
    def put(self, request, pk, format=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('updated')
        return Response(serializer.errors)
    
    def patch(self, request, pk, format= None):
        id=pk
        stu= Student.objects.get(id=id)
        serializer=StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('partially updated')
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response('deleted')


class StudentGenericList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Student.objects.all()
        serializer=StudentSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset=Student.objects.get(id=pk)
        serializer=StudentSerializer(queryset)
        return Response(serializer.data)
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("saved")
        return Response(serializer.errors)
    def update(self, request, pk=None):
        instance = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


class InstructorModelViewSet(viewsets.ModelViewSet):
    queryset=Instructor.objects.all()
    serializer_class=InstructorSerializer

class SingerModelViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

class SongModelViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer


filedata = {
  'apiKey': "AIzaSyDWRsJY1s3INaXOlfWKZ8rhOAo_BpuicY8",
  'authDomain': "testproject-61ca2.firebaseapp.com",
  'projectId': "testproject-61ca2",
  'storageBucket': "testproject-61ca2.appspot.com",
  'messagingSenderId': "710261833852",
  'appId': "1:710261833852:web:8fe10b425f6bb399eec9f9",
  'measurementId': "G-VG1EN1FHE7"
}

def message(request):
    return render(request,'message.html')

