# 시간을 줄이는 전략
1. .~ attribute를 지나치게 많이 반복하면 느려진다.
   (도저히 답이 안나올때 참고.)
   (따로 변수에 할당해서 쓰는게 나은거 같다는데)
   (직접 실험해보니 아닌듯..)
   
```python
arr=[]
#이런식으로 써야 빨라진다고는 함(?)
ap = arr.append ; ap(3)

#아래처럼 하면 오히려 느려진다.
lp = list.append ; lp(arr,3) #
```
2. 1 씩 증감 하지말고 bisection 접근법 활용

3. a = open(0) 을 활용해서 입력 한꺼번에 받기 가능
입력이 매우 많을때 1개씩 받으면 그 속도가 매우 느려짐
(10만개 정도만 되도 input 받아오는 시간
신경써야 함.)

4. 아래와 같이 입력을 받으면 속도가 빠르다고 한다.
`import io, import os`
`io.BytesIO(os.read(0, os.fstat(0).st_size)).readline`
#참고 링크
https://stackoverflow.com/questions/60594617/fastest-way-to-read-many-inputs-in-pypy3-and-what-is-bytesio-doing-here
#메모리가 4MB 급 극단적으로 제한되는 상황에선 그냥 sys가 나음(메모리 초과)

5. 특이한 형태 `->` 이는 함수에서 단순히 리턴값의 형태에 대한 주석이다.
리턴값의 형태를 알려줄뿐 아무런 영향도 없다.
진짜 주석이라 자료형아니라도 아무거나 막쳐도 된다.
```
def s(x) -> str:
    return x
def s(x) -> 3215132421312:
   return x
```

6. 메모리 제한(보통 코딩문제 128~256MB 정도지만 가끔 4MB 이딴식으로
극단적으로 제한적인 case 존재, ex = boj_11723번
이렇게 메모리가 극단적으로 제한되거나 메모리를 아껴야 하면
메모리를 효율적으로 관리하는 python3로 실행권장.
pypy는 python3와 가비지콜렉터 구조가 달라서
크기를 대략적으로 할당하는 등, 경험상 메모리 소모 3배 정도 차이남.