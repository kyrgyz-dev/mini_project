from django.urls import path
from user.views import registration, login_view, logout_view, profile_view

app_name = 'user'
urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login_view, name='login'), #user:login
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
