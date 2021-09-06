  
from django.urls import path

from .views import PostsListView , PostsDetailView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('<int:pk>', PostsDetailView.as_view(), name='posts_details'),
]