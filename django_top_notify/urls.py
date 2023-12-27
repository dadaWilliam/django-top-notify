from django.urls import path

from . import views

app_name = "django_top_notify"

urlpatterns = [
    path("latest_system_notification/", views.get_latest_system_notification, name="latest_system_notification"),
]
