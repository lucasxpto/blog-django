from django.urls import path

from .views import PostDetailView

urlpatterns = [
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
