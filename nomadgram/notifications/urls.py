from . import views
from django.urls import path

app_name = "notifications"
urlpatterns = [
    path(
        "",
        view=views.NotificationView.as_view(),
        name='notification'
    )
]