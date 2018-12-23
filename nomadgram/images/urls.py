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
        "<int:image_id>/unlike/",
        view=views.UnLikeView.as_view(),
        name='unlike_view'
    ),
    path(
        "<int:image_id>/comment/",
        view=views.CommentOnImage.as_view(),
        name='comment_on_image'
    ),
    path(
        "<int:image_id>/comment/<int:comment_id>",
        view=views.ModerateComment.as_view(),
        name='moderate_comment'
        #delete comment on my image
    ),
    path(
        "comment/<int:comment_id>",
        view=views.Comment.as_view(),
        name='comment'
        #delete comment by user_id
    ),
    path(
        "search/",
        view=views.Search.as_view(),
        name='search'
    )
]
