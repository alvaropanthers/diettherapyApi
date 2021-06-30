from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def auth_user(request):
    print("HITTTT")
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