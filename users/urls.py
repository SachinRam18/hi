from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('rooms/', views.room_list, name='room_list'),
    path('chat/<str:room_name>/', views.chat_room, name='chat'),
]
