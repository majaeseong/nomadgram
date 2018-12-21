from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models

class FeedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )

class CommentSerializer(serializers.ModelSerializer):

    #image = ImageSerializer()
    creator = FeedUserSerializer()

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )

class LikeSerializer(serializers.ModelSerializer):

    #image = ImageSerializer() # we get all fields, but we dont want to get forien key

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Like
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    #likes = LikeSerializer(many=True)
    #models의 related_name을 통해서 이름을 변경할 수 있다.
    #원래는 comment_set, like_set 
    creator = FeedUserSerializer()

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator'
        )