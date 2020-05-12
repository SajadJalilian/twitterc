from django.urls import path
from .views import (
    StatusListView,
    StatusDeleteView,
    StatusDetailView,
    UserStatusListView,
)

from . import views


urlpatterns = [
    path("", StatusListView.as_view(), name="mytwitter-home"),
    path("status/<int:pk>/", StatusDetailView.as_view, name="status-detail"),
    path("status/<int:pk>/delete/", StatusDeleteView.as_view, name="user-delete"),
    path("user/<str:username>/", UserStatusListView.as_view, name="user-statuses"),
    path("about/", views.about, name="mytwitter-about"),
]
