import itertools as it
import operator
#기본적으로 itertools로 만든 놈들은 대부분 iterator

#chain = # iteralble 들을 *args 인자로 받고 전부 이어 붙인
# iterator를 만든다
print("*********** chain 예제 ******************")
a = it.chain("안녕하세요","강기한입니다.")# 이런 단순한 예보다는 2차원 배열에 유용할 듯
print(list(a)) #list는 먹히고 str은 iterator 객체를 반환함
for i in a:
    print(i) #for나 while next 활용 가능 list같은거로 리스트로 만들수도 있음
print("*****************************************\n")

#accumulate 누적합 편하게 해보자
print("*********** accumlate 예제 ******************") #reduce와 비슷하지만 이녀석은 리스트 보존
b = [1,2,3,4,5,6,7,8,9,10]
print(list(it.accumulate(b)))
print(list(it.accumulate(b,initial=100)))
print(list(it.accumulate(b,operator.mul)))
# operator의 method가 생각보다 다양함.
# operator 함수 뿐만 아니라 lambda 식도 활용 가능
# 팩토리얼 구현도 쉬울듯
print("*****************************************\n")

print("*********** product 예제 ******************")
#각 행렬 요소를 이어 붙인 결과를 만든다 중첩 for 문과 같음.
#repeat로 중첩시키기도 가능.
#쉽게 여러 리스트의 곱셈 결과를 출력 가능
print(list(it.product([1,2,3],[4,5,6],[7,8,9])))#
print("*****************************************\n")

#zip할때 길이가 딸린부분 자동으로 채워주는 개꿀 템
print("*********** zip_longest 예제 ******************")
d = ["abcde","fgh","ez","q"]
print(list(it.zip_longest(*d,fillvalue="")))
#이러면 가로읽기 아주 쉬워지죠?
#padding도 쉬워짐
print("*****************************************\n")

print("*********** cyle 예제 ******************")
#시작과 끝이 연결된 계속 순환되는 객체를 반환
e = it.cycle([1,2,3,4,5])
for i in range(10):
    print(next(e),end=" ") #계속 순환해야할 일이 있을때 유용할 듯
print("\n*****************************************\n")

print("*********** dropwhile 예제 ******************")
f = [1,2,3,4,5,6,7,1,2,3,4]
#리스트에서 어떤 조건이 참일때 부터 리스트를 출력하고 싶다?
print(list(it.dropwhile(lambda x: x != 6, f))) #1줄로 간단하게
#위는 x==6일때부터 리스트 만든다는 뜻
print("*****************************************\n")

print("*********** takewhile 예제 ******************")
#리스트에서 어떤 조건이 참일때 까지 리스트를 출력하고 싶다?
print(list(it.takewhile(lambda x: x != 6, f))) #1줄로 간단하게
#위는 x==6일때부터 리스트 만든다는 뜻
print("*****************************************\n")

print("*********** filterfalse 예제 ******************")
#1부터 10까지 숫자중 짝수가 아닌것만 걸러내기, 기본 내장함수인 filter와 유사
print(list(it.filterfalse(lambda x: x%2==0, range(1,11))))
#거짓인것만 걸러내주니까 헥갈려서 filter 함수 쓰는게 오히려 편할지도?
print("*****************************************\n")

print("*********** compress 예제 ******************")
#필요한 iterable과 true false 요소 iterable을 압축시켜 출력
#binary하게 부분집합 구할때 꿀팁인듯
g = "우리나라"
bins = []
for i in range(1<<4): #4자리 이진수만들기
    print( list(it.compress(g,map(int,f'{i:04b}'))) ) # 아주 깔끔하게 부분집합 생성가능.
print("*****************************************\n")

print("*********** starmap 예제 ******************")
#그냥 map(함수, iteralbe) 인데
#starmap(함수, iteralbe) 로 같아 보이지만 iterable 내보의 iterable을 unzip해서 함수 적용
h = [(1,2,3), (2,3,4), (4,5,5)] # 리스트의 요소가 길이가 2여야 작동,
# *args 형태로 인자를 받는 함수에 적용 가능.
list(it.starmap(print , h)) #2차원 리스트 한줄로 깔끔하게 출력 가능
# iterable은 list나 tuple등으로 만드는 순간 전부 메모리 위로 올라가서 함수가 실행됨.
print("*****************************************\n")


print("*********** pairwise 예제 ******************") # 3.10버전 부터 사용가능
h = "abcdefghijklmnopqrxtuvwxyz"                      # 범용성 떨어지지만
#print(list(it.pairwise(h)))  # iterable을 2개씩 묶어준다.
#ex) '1234' = ('1','2'), ('3','4')
print("*****************************************\n")