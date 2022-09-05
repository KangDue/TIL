from django.db import models

# Create your models here.
class Question(models.Model):
  subject = models.CharField(max_length = 200) #길이 제한
  content = models.TextField() # 텍스트 받기(길이 제한 불가능)
  create_date = models.DateTimeField() # 날짜 받기

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE) #기존 모델을 속성으로 연결 -key를 Question에서 받는다, 삭제하면 Cascade 한다.(낙수? 질문 삭제시 같이 삭제)
  content = models.TextField()
  create_date = models.DateTimeField() # 날짜 받기