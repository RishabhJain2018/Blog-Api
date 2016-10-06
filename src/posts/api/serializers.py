from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from posts.models import Post


class PostCreateUpdateSerializer(serializers.ModelSerializer):
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
    url = HyperlinkedIdentityField(
        view_name = 'posts-api:detail',
        lookup_field='slug',
        )

    delete_url = HyperlinkedIdentityField(
        view_name = 'posts-api:delete',
        lookup_field='slug',
        )
    class Meta:
        model = Post
        fields = [
        'url',
        'user',
        'id',
        'title',
        'slug',
        'content',
        'publish',
        'delete_url',
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