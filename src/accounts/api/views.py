from .serializers import (
	UserCreateSerializer,
	UserLoginSerializer,
	)

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView,
	)

from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.permissions import (
	AllowAny,
	)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()


class UserLoginAPIView(APIView):
	permissions_classes = [AllowAny]
	serializer_class =UserLoginSerializer
	
	def post(self, request, *args, **kwargs):
		data = request.data #request.POST
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

