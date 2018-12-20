from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass # it means empty class
    #데코레이터에 의해 자동으로 됨.

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass # it means empty class

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass # it means empty class