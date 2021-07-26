from django.http.response import Http404
from django.shortcuts import render
from rest_framework import HTTP_HEADER_ENCODING, generics
from .models import User, PhysicalActivity
from .serializers import UserSerializer, PhysicalActivitySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def auth_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(email=data['email'], password=data['password'])
            return JsonResponse({"authenticated": True, "id": user.id})
        except Exception:
            return JsonResponse({"authenticated": False})

class UserList(generics.ListCreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def physical_activity(request):
    data = JSONParser().parse(request)

    if request.method == 'POST':
        try:
            user = User.objects.get(pk=data['user_id'])
            pa = PhysicalActivity(user=user, activityType=data['activityType'], activityName=data['activityName'])
            pa.save()
            return JsonResponse({"created": True}) 
        except Exception:
            return JsonResponse({"created": False})
    elif request.method == 'GET':
        try:
            user = User.objects.get(pk=data['user_id'])
            pa = PhysicalActivity.objects.get(user=user, activityType=data['activityType'].lower())
            serializer = PhysicalActivitySerializer(pa, many=True)
            return JsonResponse(serializer.data)
        except Exception:
            return Http404()

# class PhysicalActivity(generics.ListCreateAPIView):
#     permission_classes = ()
#     authentication_classes = ()
#     lookup_url_kwarg = 'user_id'
#     queryset = PhysicalActivity.objects.all()
#     serializer_class = PhysicalActivitySerializer