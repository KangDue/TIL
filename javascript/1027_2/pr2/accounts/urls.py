from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('update/',views.update,name='update'),
    path('password/',views.password_change,name='password_change'),
    path('<str:username>/profile/',views.profile,name='profile'),
    path('<str:username>/follow/',views.follow,name='follow'),
]
