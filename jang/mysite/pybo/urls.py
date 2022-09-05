from django.urls import path, include

from . import views

app_name = 'pybo'
urlpatterns = [   ## pybo/ + ''
    path('',views.index,name = 'index'), ##config.urls에서 이미 pybo/를 해놔서 ''만씀
    path('<int:question_id>/',views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/',views.answer_create, name = "answer_create"),
]
