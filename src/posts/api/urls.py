from django.conf.urls import url
from django.contrib import admin


from .views import (
	PostListAPIView,
	PostDetailAPIView
	)


urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
	url(r'^(?P<abc>[\w+]+)/$', PostDetailAPIView.as_view(), name='detail'),
]
