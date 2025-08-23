from django.urls import path
from post.views import create_post, delete_post, detail_post, edit_post

app_name = 'post'
urlpatterns = [
    path('create/', create_post, name='create-post'),
    path('<int:pk>/', detail_post, name='detail-post'),
    path('<int:pk>/edit/', edit_post, name='edit-post'),
    path('<int:pk>/delete/', delete_post, name='delete-post'),
]
