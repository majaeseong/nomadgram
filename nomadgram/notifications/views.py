from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
# Create your views here.

class NotificationView(APIView):

    def get(self, request, format=None):
        
        user = request.user

        notis = models.Notification.objects.filter(to=user)

        serializer = serializers.NotificationSerializers(notis, many=True)

        return Response(data=serializer.data)


#view는 만들지 않는다. 다른 사람이 내 알림을 보면 안되니깐 -> function

def create_notification(creator, to, notification_type, image=None, comment=None):

    new_notification = models.Notification.objects.create(
        creator=creator,
        to=to,
        notification_type=notification_type,
        image=image,
        comment=comment
    )
    new_notification.save()