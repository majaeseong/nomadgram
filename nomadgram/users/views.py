from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ExploreUser(APIView):
    
    def get(self, request, format=None):
        last_five = models.User.objects.all().order_by('-date_joined')[:5]

        serializer = serializers.ExporeUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=200)

class FollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            following_user = models.User.objects.get(id=user_id)

        except models.User.DoesNotExist:
            return Response(status=404)

        user.followings.add(following_user)
        user.save

        return Response(status=200)

class UnFollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            following_user = models.User.objects.get(id=user_id)

        except models.User.DoesNotExist:
            return Response(status=404)

        user.followings.remove(following_user)
        user.save

        return Response(status=200)