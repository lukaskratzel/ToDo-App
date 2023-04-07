from django.urls import path
from . import views

app_name = "feed"

urlpatterns = [
    path("", views.FeedView.as_view(), name='index'),
    path("delete/", views.DeleteView.as_view(), name='delete')
]