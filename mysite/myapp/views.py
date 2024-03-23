# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User


def list_users(request):
    users = User.objects.all()
    return render(request, 'myapp/user_details.html', {'users': users})


# views.py
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
