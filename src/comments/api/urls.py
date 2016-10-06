from django.conf.urls import url
from django.contrib import admin

from comments.api.views import (
	CommentListAPIView,
	CommentDetailAPIView,
    )

urlpatterns = [
	url(r'^$', CommentListAPIView.as_view(), name='list'),
	url(r'^(?P<id>\d+)$', CommentDetailAPIView.as_view(), name='thread'),


]
