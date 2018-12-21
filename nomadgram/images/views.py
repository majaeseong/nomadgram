from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class Feed(APIView):

    def get(self, request, format=None):

        user =request.user
        following_users = user.followings.all()

        image_list=[]

        for follo in following_users:
            user_images = follo.images.all()[:2]
            
            for img in user_images:
                image_list.append(img)

        sorted_list = sorted(image_list,key=lambda image : image.created_at, reverse=True)
        
        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(data = serializer.data)


class LikeView(APIView):

    def get(self, request, image_id,format=None):

        print(image_id)

        return Response(status=200)