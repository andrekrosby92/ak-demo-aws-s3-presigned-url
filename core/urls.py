from django.contrib import admin
from django.urls import path

from .views import GetPresignedURLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-presigned-url/', GetPresignedURLView.as_view()),
]
