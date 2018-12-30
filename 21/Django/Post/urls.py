from django.conf.urls import url
from django.urls import path
from Post import views
urlpatterns = [
    path(r'post/', views.postList)
]
