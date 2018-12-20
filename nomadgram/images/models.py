from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #for the first
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #database와 연결되지 않음.
        #다른 클래스를 위해 base가 됨 - 재사용 효율성

class Image(TimestampedModel):
    """ Image Model """
    file = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

class Comment(TimestampedModel):
    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

class Like(TimestampedModel):
    """ Like Model """
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)