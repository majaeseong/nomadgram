from rest_framework import serializers
from . import models
from nomadgram.images import serializers as images_serializers

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields=(
            'id',
            'profile_image',
            'username',
            'name'
        )

class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializers.CountImageSerializer(many=True)
    post_count = serializers.ReadOnlyField()
    followings_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    #ReadOnlyField-> 수정하지 않겠다!

    class Meta:
        model = models.User
        fields=(
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followings_count',
            'followers_count',
            'images'
        )
