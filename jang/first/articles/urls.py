from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('greeting/',views.greeting,name='greeting'),
    path('dinner/',views.dinner,name='dinner'),
    path('throw/',views.throw,name='throw'),
    path('catch/',views.catch,name="catch"),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update/',views.update,name='update'),
]
