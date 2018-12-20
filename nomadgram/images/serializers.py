from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Image
        fields = '__all__'

class CommentSerializer(serializers.Serializer):

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.Serializer):

    class Meta: # Meta is extra data, 설정을 위한 클래스
        model = models.Like
        fields = '__all__'