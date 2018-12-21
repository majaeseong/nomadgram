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

    def post(self, request, image_id,format=None):

        found_image = invalid_image(image_id)

        try:
            preexisting_like = models.Like.objects.get(
                creator=request.user,
            image = found_image
            )
            return Response(status=304)

        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator=request.user,
                image = found_image
            )
            new_like.save()

            return Response(status=201)

class UnLikeView(APIView):
    def delete(self, request, image_id,format=None):
        found_image = invalid_image(image_id)

        try:
            preexisting_like = models.Like.objects.get(
                creator=request.user,
            image = found_image
            )
            preexisting_like.delete()
            return Response(status=204)

        except models.Like.DoesNotExist:
            return Response(status=304)


class CommentOnImage(APIView):
    def post(slef, request, image_id, format=None):

        try:
            found_image = invalid_image(image_id)
        except models.Image.DoesNotExist:
            return Response(status=404)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(creator=request.user, image=found_image)
            return Response(data = serializer.data ,status=201)
        else:
            return Response(data = serializer.errors, status = 400)

def invalid_image(id):
    try:
        found_image = models.Image.objects.get(id=id)
        return found_image
    except models.Image.DoesNotExist:
        return Response(status=404)


class Comment(APIView):
    def delete(self, request, comment_id, format=None):
        try:
            comment = models.Comment.objects.get(id=comment_id, creator = request.user)
            comment.delete()
            return Response(status=204)
        except models.Comment.DoesNotExist:
            return Response(status=404)