from main.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singers/', SingerAPIView.as_view()),
    path('singers/<int:pk>/', SignerRetrieveUpdateAPIView.as_view()),
    path('songs/', SongsAPIView.as_view()),
]
