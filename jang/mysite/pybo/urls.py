from django.urls import path, include

from . import views
urlpatterns = [   ## pybo/ + ''
    path('',views.index), ##config.urls에서 이미 pybo/를 해놔서 ''만씀
]
