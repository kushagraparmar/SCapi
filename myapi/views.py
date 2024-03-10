from django.shortcuts import render
from .models import Register, CourseContent,ParticularCourse,Paid_Course_Content
from . import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import random


@api_view(['get'])
def home(request):
    data=CourseContent.objects.all()
    serializer=serializers.CourseSerializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['get'])
def Course(request,id):
    data=ParticularCourse.objects.filter(pk=id)
    serializer=serializers.ParticularCourseSerializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

@api_view(['post'])
def CallRequest(request):
    if request.method=="POST":
        serializer = serializers.InquerrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'ERROR':"Warning Error"},status=status.HTTP_204_NO_CONTENT)

@api_view(['post','put'])
def register(request):
  global datass 
  global serializer_register
  if request.method == 'POST':
       datass=request.data
       serializer_register=serializers.RegisterSerializer(data=request.data)
       email=request.data['email']
       if serializer_register.is_valid():
            serializer_register.save()
            if email != None:
                a=random.randint(5241,9879)
                dot=Register.objects.get(email=datass['email'])
                dot.otp =a
                dot.save()
                send_mail('For Verification to Shiva Concept Digital',f'Your Verification Code is . . . . {a}','settings.EMAIL_HOST_USER',[email],fail_silently=False)
                return Response({"Wait":"Waiting for email verification"},status=status.HTTP_202_ACCEPTED)
  if request.method == 'PUT':
    ab=Register.objects.get(email=datass['email'])
    otpenter=request.data['name']
    if otpenter == ab.otp:
        return Response(serializer_register.data,status=status.HTTP_201_CREATED)
    else:
        ab.delete()
        return Response({"Wrong":"Wrong Otp"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
  return Response({"Not":"Not Created"},status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['post'])
def Login(request):
    if request.method=='POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = None
        if not user :
            user=Register.objects.filter(email=email , password=password)
        if user:
            return Response({"Success":"Successfully"},status=status.HTTP_202_ACCEPTED)
        return Response({"Error":"Wrong Input"},status=status.HTTP_400_BAD_REQUEST)

def test(request):
    if request.method =='POST':
        email=request.POST['email']
        a=random.randint(1000,9999)
        send_mail(
            'Verification',
            f'Hi i am a bot i want to need this otp   . . . . . . . . {a}',
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
        return render(request,'test/ver.html')
    return render(request,'test/home.html')

def check(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if otp == None:
            return HttpResponse('Verified')
        return  HttpResponse(f'wrong otp {otp} <br> ')
    
@api_view(['post','put'])   
def tes(request):
    if request.method == 'PUT':
        print(request.data['name'])
    return  HttpResponse('wrong otp')

@api_view(['get'])
def test2(request):
    data=Paid_Course_Content.objects.filter(Select="Python")
    serializer=serializers.Paid_Course_Content_Serializers(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)