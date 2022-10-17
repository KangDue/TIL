from rest_framework import serializers
from .models import Article,Comment

#목록, 쿼리셋 시리얼라이저 , 단일 항목은 다른거로 해야함.
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content',)
#쿼리셋 시리얼라이즈는 many = True 필수

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer): #to many rel(1:N의 관계가 (개수x) 중요한 것) 
    # comment_set = serializers.PrimaryKeyRelatedField(many=True)
    comment_set = CommentSerializer(many=1, read_only=1) #그대로 참조
    
    #source값에 orm명령어를 넣어주면 된다. instance명, () 생략
    #필드를 채우는데 사용할 속성의 이름
    # . notation으로 찾을 수 있음
    comment_count = serializers.IntegerField(source='comment_set.count',read_only=1)
    class Meta:
        model = Article
        fields = '__all__'
        

#상황에 맞는 시리얼라이저 가져다쓰고 상속받고 할 수 있게 잘 설계
#read_only 유효성검사는 제외하지만 읽긴 함.
#override 또는 별도로 추가된 것들은 Meta에서 read_only 할 수 없음
#각각 필드상에서 바로 정의해야햠.