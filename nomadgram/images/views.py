from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

#Test Serializer - View
class AllImage(APIView):
    def get(self, request, format=None):
        all_images = models.Image.objects.all()
        serialzier = serializers.ImageSerializer(all_images, many=True)

        return Response(data = serialzier.data)

class AllComment(APIView):
    def get(self, request, format=None):
        all_comment = models.Comment.objects.all()
        serialzier = serializers.CommentSerializer(all_comment, many=True)

        return Response(data = serialzier.data)

class AllLike(APIView):
    def get(self, request, format=None):
        all_like = models.Like.objects.all()
        serialzier = serializers.LikeSerializer(all_like, many=True)

        return Response(data = serialzier.data)