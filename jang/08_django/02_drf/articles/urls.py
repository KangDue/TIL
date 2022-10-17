from django.urls import path
from . import views


 #템플릿 안쓸거니 app_name, name 무쓸모
 #뒤의 /를 다 붙여주자 외부에서 작동하는 프로그램들은 자동으로 / 안붙임.
urlpatterns = [
    path('articles/',views.article_list),
    path('articles/<int:article_pk>/',views.article_datail),
    path('comments/',views.comment_list),
    path('comments/<int:comment_pk>/',views.comment_detail),
    path('articles/<int:article_pk>/comments/',views.comment_create),
]
