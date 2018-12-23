from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from nomadgram.notifications import views as notification_views
from nomadgram.users import models as user_models
from nomadgram.users import serializers as user_serializers

class Feed(APIView):

    def get(self, request, format=None):

        user =request.user
        following_users = user.followings.all()

        image_list=[]

        for follo in following_users:
            user_images = follo.images.all()[:2]
            
            for img in user_images:
                image_list.append(img)

        my_images = user.images.all()[:2]

        for img in my_images:
            image_list.append(img)

        sorted_list = sorted(image_list,key=lambda image : image.created_at, reverse=True)
        
        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(data = serializer.data)

class ImageDetail(APIView):
    #class 안의 function은 self 반드시 필요 
    def find_own_image(self,image_id, user):
        try:
            found_image = models.Image.objects.get(id=image_id, creator=user)
            return found_image
        except models.Image.DoesNotExist:
            return None

    def get(self, request, image_id, format=None):

        found_image = invalid_image(image_id)

        serializer = serializers.ImageSerializer(found_image)

        return Response(data=serializer.data)

    def put(self, request, image_id, format=None):

        user=request.user
        found_image = self.find_own_image(image_id, user)

        if found_image is None:
            return Response(status = 401)
        
        serializer = serializers.InputImageSerializer(found_image,
            data=request.data, partial=True)
            #partial -> 부분 저장, 필수요소들 다 입력하지 않아도 해당하는 것만 변경해줄 수 있게 해줌.
        
        if serializer.is_valid():
            serializer.save(creator=user)
            return Response(data=serializer.data, status=200)
        else:
            return Response(status=400)

    def delete(self, request, image_id, format=None):

        user=request.user
        found_image = self.find_own_image(image_id, user)

        if found_image is None:
            return Response(status = 401)

        found_image.delete()
        return Response(status = 204)





class LikeView(APIView):

    def get(self, request, image_id, format=None):

        likes= models.Like.objects.filter(image__id = image_id)

        users = user_models.User.objects.filter(id__in = likes.values('creator_id'))

        serializer = user_serializers.ListUserSerializer(users, many=True)

        return Response(data = serializer.data, status=200)



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
            #notification
            notification_views.create_notification(request.user, found_image.creator, 'like', found_image)

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

            #notification
            notification_views.create_notification(request.user, found_image.creator, 'comment', found_image, serializer.data['message'])
                                                                                                                #= request.data['message']

            return Response(data = serializer.data ,status=201)
        else:
            return Response(data = serializer.errors, status = 400)


class Comment(APIView):
    def delete(self, request, comment_id, format=None):
        try:
            comment = models.Comment.objects.get(id=comment_id, creator = request.user)
            comment.delete()
            return Response(status=204)
        except models.Comment.DoesNotExist:
            return Response(status=404)

class ModerateComment(APIView):
    def delete(self, request, image_id, comment_id, format=None):
    
        try:
            comment = models.Comment.objects.get(id=comment_id,
                image__id=image_id, image__creator=request.user)
            comment.delete()
            return Response(status=204)
        except models.Comment.DoesNotExist:
            return Response(status=404)

class Search(APIView):
    def get(self, request, format=None):

        hash_tags = request.query_params.get('hashtags',None)
        
        if hash_tags is not None:
            hash_tags = hash_tags.split(',')
        
            images= models.Image.objects.filter(tags__name__in=hash_tags).distinct()
            #deep(nested) relationship
            # creator__username = admin
            # creator__username__contains = ad -> 대소문자 구분 icontains -> 구분 X

            serializer = serializers.CountImageSerializer(images, many=True)

            return Response(data = serializer.data, status=200)
        else :
            return Response(status=400)





def invalid_image(id):
    try:
        found_image = models.Image.objects.get(id=id)
        return found_image
    except models.Image.DoesNotExist:
        return Response(status=404)