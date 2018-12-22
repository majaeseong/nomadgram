from django.db import models
from nomadgram.users import models as user_models
from nomadgram.images import models as images_models
# Create your models here.

class Notification(images_models.TimestampedModel):

    TYPE_CHOICES=(
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow')
        #first- for use on database, second - for use on admin pannel
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='creator')
    to = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='to')
    #같은 외래키를 사용해서 반드시 realted_name을 지정해주어야 한다.
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(images_models.Image, on_delete=models.CASCADE, null=True,blank=True)
    comment = models.TextField(null=True,blank=True)