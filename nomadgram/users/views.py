from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from nomadgram.notifications import views as notification_views
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class ExploreUser(APIView):
    
    def get(self, request, format=None):
        last_five = models.User.objects.all().order_by('-date_joined')[:5]

        serializer = serializers.ListUserSerializer(last_five, many=True)

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

        #notification
        notification_views.create_notification(user,following_user,'follow')

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

class UserProfile(APIView):

    def find_user(self, username):
        try:
            found_user = models.User.objects.get(username=username)
            return found_user
        except models.User.DoesNotExist:
            return None

    def get(self, request, username, format=None):

        found_user = self.find_user(username)
        if found_user is None:
            return Response(status=404)

        serializer = serializers.UserProfileSerializer(found_user)

        return Response(data=serializer.data, status=200)

    def put(self, request, username, format=None):

        user = request.user

        found_user = self.find_user(username)
        if found_user is None:
            return Response(status=404)
        elif found_user.username != user.username :
            return Response(status=401)

        serializer = serializers.UserProfileSerializer(found_user, 
            data = request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        else:
            return Response(data=serializer.errors,status=404)
        


class UserFollowers(APIView):
    def get(self, request, username, format=None):

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=404)

        user_followers = found_user.followers.all()

        serializer = serializers.ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=200)

class UserFollowings(APIView):
    def get(self, request, username, format=None):

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=404)

        user_followings = found_user.followings.all()

        serializer = serializers.ListUserSerializer(user_followings, many=True)

        return Response(data=serializer.data, status=200)

class Search(APIView):

    def get(self, request, format=None):
        username = request.query_params.get('username',None)
        if username is not None:
            users = models.User.objects.filter(username__istartswith=username)
            print(username)
            print(users)
            serializer = serializers.ListUserSerializer(users, many=True)

            return Response(data=serializer.data, status=200)
        else:
            return Response(status=400)

class ChangePassword(APIView):
    
    def put(self, request, username, format=None):

        user = request.user

        current_password = request.data.get('current_password',None)
        #if can't find data = None

        if username == user.username:
            if current_password is not None:
                password_match = user.check_password(current_password)
                            #Bool
                if password_match:
                    new_password = request.data.get('new_password',None)

                    if new_password is not None:
                        user.set_password(new_password)
                        user.save()
                        return Response(status=200)
                    else:
                        return Response(status=400)

                else:
                    return Response(status=400)

            else:
                return Response(status=400)
        else:
            return Response(status=401)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter