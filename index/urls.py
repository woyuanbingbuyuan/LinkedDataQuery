from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('expand', views.expand),
    path('upload', views.upload),
    path('comment', views.add_comment),
    path('public_data', views.get_public_data),
]