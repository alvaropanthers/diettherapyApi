from django.http.response import Http404
from django.shortcuts import render
from rest_framework import HTTP_HEADER_ENCODING, generics
from .models import User, PhysicalActivity, Measurements
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
            user = User.objects.get(email=data['email'])
            if data['password'] == user.password:
                print("Authenticated!")
                userSerializer = UserSerializer(user)
                return JsonResponse(userSerializer.data)

        except Exception:
            pass

    return JsonResponse(None, safe=False)


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
def physical_activity(request, user_id=None):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(pk=data['user_id'])
            pa = PhysicalActivity(user=user, activityType=data['activityType'].lower(), activityName=data['activityName'].lower())
            pa.save()
            return JsonResponse({"created": True}) 
        except Exception:
            return JsonResponse({"created": False})
    elif request.method == 'GET':
        try:
            user = User.objects.get(pk=user_id)
            hobbies = PhysicalActivity.objects.filter(user=user, activityType='hobbies')
            favorite = PhysicalActivity.objects.filter(user=user, activityType='favorite')
            events = PhysicalActivity.objects.filter(user=user, activityType='events')
            bestActivities = PhysicalActivity.objects.filter(user=user, activityType='bestactivities')
            # serializer = PhysicalActivitySerializer(pa, many=True)
            hobbiesSerializer = PhysicalActivitySerializer(hobbies, many=True)
            favoriteSerializer = PhysicalActivitySerializer(favorite, many=True)
            eventSerializer = PhysicalActivitySerializer(events, many=True)
            bestActivitiesSerializer = PhysicalActivitySerializer(bestActivities, many=True)
            return JsonResponse({
                "hobbies": hobbiesSerializer.data, 
                "favorite": favoriteSerializer.data,
                "event": eventSerializer.data,
                "bestactivities": bestActivitiesSerializer.data
            }, safe=False)
        except Exception as e:
            return Http404()

@csrf_exempt
def measurements(request, user_id=None):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(pk=data['user_id'])
            m = Measurements(
                user=user,
                MAC=data['mac'],
                WC=data['wc'],
                HC=data['hc']
            )
            m.save()
            return JsonResponse({"created": True}) 
        except Exception:
            return JsonResponse({"created": False})

# class PhysicalActivity(generics.ListCreateAPIView):
#     permission_classes = ()
#     authentication_classes = ()
#     lookup_url_kwarg = 'user_id'
#     queryset = PhysicalActivity.objects.all()
#     serializer_class = PhysicalActivitySerializer