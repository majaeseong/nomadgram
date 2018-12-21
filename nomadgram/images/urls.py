from django.conf.urls import url
from . import views
from django.urls import path

app_name = "images"
urlpatterns = [
    path(
        "",
        view=views.Feed.as_view(),
        name='feed'
    ),
    path(
        "<int:image_id>/like/",
        view=views.LikeView.as_view(),
        name='like_view'
    ),
    path(
        "<int:image_id>/comment/",
        view=views.CommentOnImage.as_view(),
        name='comment_on_image'
    )
]
