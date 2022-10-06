from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:article_pk>/detail/',views.detail,name='detail'),
    path('<int:article_pk>/comment/',views.comment_create,name='comment_create'),
    path('<int:article_pk>/<int:comment_pk>/comment/',views.comment_delete,name='comment_delete'),
    path('<int:article_pk>/delete',views.delete,name='delete'),
]
