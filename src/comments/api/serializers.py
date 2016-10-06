from rest_framework import serializers
from comments.models import Comment

from rest_framework.serializers import (
    HyperlinkedIdentityField, 
    SerializerMethodField,
    )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
        'id',
        'content_type',
        'object_id',
        # 'content_object',
        'parent',
        'content',
        ]
