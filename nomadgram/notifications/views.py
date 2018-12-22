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