from rest_framework import serializers
from posts.models import Post

from rest_framework.serializers import (
    HyperlinkedIdentityField, 
    SerializerMethodField,
    )



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
    user = SerializerMethodField()
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
        'user',
        'id',
        'title',
        'slug',
        'content',
        'markdown',
        'publish',
        'image',
        ]

    def get_markdown(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image


class PostListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'posts-api:detail',
        lookup_field='slug',
        )

    delete_url = HyperlinkedIdentityField(
        view_name = 'posts-api:delete',
        lookup_field='slug',
        )

    user = SerializerMethodField()
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

    def get_user(self, obj):
        return str(obj.user.username)




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