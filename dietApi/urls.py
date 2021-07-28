from django.urls import path
from dietApi import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('auth/', csrf_exempt(views.auth_user)),
    path('users/', csrf_exempt(views.UserList.as_view())),
    path('users/<int:pk>/', csrf_exempt(views.UserDetails.as_view())),
    path('physical/', csrf_exempt(views.physical_activity)),
    path('physical/<int:user_id>/', csrf_exempt(views.physical_activity)),
    path('measurements/', csrf_exempt(views.measurements))
]