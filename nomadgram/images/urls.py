from django.conf.urls import url
from . import views

app_name = "images"
urlpatterns = [
    url(
        regex="all/",
        view=views.AllImage.as_view() , #AllImage is class, so add as_view
        name='all_images'
    ),
    url(
        regex="comment/",
        view=views.AllComment.as_view() , #AllImage is class, so add as_view
        name='all_comment'
    ),
    url(
        regex="like/",
        view=views.AllLike.as_view() , #AllImage is class, so add as_view
        name='all_like'
    )
]
