from django.urls import path
from . import views
#https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-2/
#특정 url 변경하기
app_name = 'accounts'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('delete/',views.delete,name='delete'),
    path('update/',views.update,name='update'),
    path('password/',views.change_password,name='change_password'),
    path('<str:username>/profile/',views.profile,name='profile'),
    path('<int:user_pk>/follow/',views.follow,name='follow'),
]
