from rest_framework.generics import (
	DestroyAPIView
	ListAPIView, 
	RetrieveAPIView,
	UpdateAPIView,
	)

from posts.models import Post
from .serializers import (
	PostCreateSerializer
	PostDetailSerializer, 
	PostListSerializer,
	)


class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer


