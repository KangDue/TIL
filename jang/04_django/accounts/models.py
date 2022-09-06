from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#일단 built-in user model 상속받고 시작
#첫 마이그레이션(migrate 실행) 전에 완료해야함
#안그러면 db를 초기화해야함. db.sqlite3 삭제
class User(AbstractUser): 
    pass