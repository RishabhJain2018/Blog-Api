from rest_framework import serializers

from posts.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
        # 'id',
        'title',
        # 'slug',
        'content',
        'publish',
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
        'id',
        'title',
        'slug',
        'content',
        'publish',
        ]

        
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
        'id',
        'title',
        'slug',
        'content',
        'publish',
        ]




"""

from posts.models import Post
from posts.api.serializers import PostDetailSerializer

data={
    "title":"Yeah Buddy",
    "content": "New Content",
    "publish": "2016-2-12",
    "slug" : "yeah-buddy"

}
obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()

else:
    print (new_item.errors)

"""