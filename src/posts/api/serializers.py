from rest_framework import serializers

from posts.models import Post


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


"""

data={
	"title":"Yeah Buddy",
	"content": "New Content",
	"publish": "2016-2-12",

}

new_item = PostSerializer(data=data)
if new_item.is_valid():
	new_item.save()

else:
	print(new_item.errors)

"""