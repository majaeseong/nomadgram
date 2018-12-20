from django.contrib import admin
from . import models
from django.utils.html import mark_safe
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    #pass # it means empty class
    #데코레이터에 의해 자동으로 됨.
    list_display_links=(
        'caption',
    )

    list_filter=(
        'creator',
    )

    list_display=(
        'showImg',
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at'
    )
    def showImg(self, obj):
        return mark_safe('<img src="{url}" width="60px"/>'.format(url = obj.file.url))
    

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    #pass # it means empty class
    list_display=(
        'creator',
        'image',
        'message',
        'created_at',
        'updated_at'
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    #pass # it means empty class
    list_display=(
        'creator',
        'image',
        'created_at',
        'updated_at'
    )