from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    #image = ImageSerializer()

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    #image = ImageSerializer() # we get all fields, but we dont want to get forien key

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    #models의 related_name을 통해서 이름을 변경할 수 있다.
    #원래는 comment_set, like_set 

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes'
        )