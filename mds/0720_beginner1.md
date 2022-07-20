# 1. 파이썬이란?

>  - 1990년 말 고안, 1991.2.20 귀도 반 로섬 발표

-  **독립적** 이며, **인터프리터 방식** 의 **객체지향** 이고, **동적**인 그리고 **대화형 성격**을 가진 프로그래밍 언어

-  Monty Python's Flying circus 라는 코미디 프로그램 에서 이름 따옴

-  파이썬의 종류

- - 1.Cpython = C기반, IronPython = C# 기반 .Net mono용, Jython = Java기반, Java 가상머신에서 작동, pypy = python으로 구현 cpython 보다 빠름.

- -  표준은 Cpython이다.

-  **<파이썬의 핵심가치>**

- -  1. 아름다운 것이 추한 것 보다 낫다.

- -  (Beautiful is better than ugly)

- - 2. 명시적인 것이 묵시적인 것보다 낫다.

- - (Explicit is better than implicit)

- - 3. 단순한 것이 복잡한 것보다 낫다.

- - (Simple is better than complex)

- - 4. 복잡한 것이 난해한 것보다 낫다.

- - (Complex is better than complicated)

- - 5. 가독성이 중요하다.

- - (Readability counts)

- <파이썬의 특징>**

- - 1.인터프리팅 방식

- - 명령의 실행결과를 대화형으로 바로 확인

- - 2. 동적 타이밍(Dynamic typing)

- - 실행 시간 값에 의해 자료형 결정

- - 3. Grabage Collector

- - 생성된 객체에 대한 메모리 관리는 Garbage Collector 이용

- - 4. 가독성(ex. 코드블록 들여쓰기)

- - 5. 풍부한 라이브러리

- - 표준 라이브러리와 통합환경이 배포판과 함께 제공

- - 정규표현식/운영 체제의 시스템 호출/ XML 처리/ 직렬화/ 각종 통신 프로토콜/ 전자 메일이나 CSV파일 처리/ 데이터베이스 접속/ 그래픽 사용자 인터페이스/ HTML, 파이썬 코드 구문 분석 도구 등등

- - 6. 유니코드

- - 7. 오픈소스 (파이썬 소프트웨어 재단에서 관리)

- - 8. 다양한 프로그래밍 패러다임 지원

- - (객체지향, 함수형 프로그래밍 지원)

- - 9. 학습 용이성

- - 프로그램의 문서화도 언어의 기본기능에 포함

- - 도움말 문서와 API도 체계적으로 정리

- - API = 운영체제가 제공하는 함수의 집합체

- - 읽기 쉽고, 효율적인 코드를 간단하게 쓰려는 철학 반영

- - 10. 내장 스크립트 언어

- - 다른 언어로 쓰인 모듈을 연결하려는 목적으로 이용되며 많은 상용 프로그램에 내장되어 스크립트 언어로 활용

- <파이썬 인기분야>**

- - 웹 애플리케이션 개발**

- - 1. Django

- - 2. Flask

- - 데이터 수집**

- - 3.Beautiful Soup

- - 4. Scrapy

- - 데이터 과학 및 인공지능**

- - 5.numpy

- - 6.pandas

- - 7.scipy (여러가지 포함)

- - 8.scikit-learn = sklearn

- - 9.tensorflow

- - 10. pytorch

- 파일은 하나의 모듈이다.

- if \_\_name__ == "\_\_main__":

- - 은 해당 파일이 main으로 실행됬을때 실행

# 2.자료형 다루기

> ### % 포매팅을 사용한 문자열 포맷팅

-  %s = 문자열, 

-  %c = 문자 하나(정수 → 유니코드문자)

- -  ord(문자)와 값이 같음. 그냥 문자 하나도 받음

- %d = 10진수, %o = 8진수, %x = 16진수

- %f = 부동소수점 ex(%6.2f), 기본적으로 소수점 아래 6자리 까지 출력

- - **부동소수점 포함** 전체자리수 10 = %10.2f

- - 빈자리 0으로 채우기 = %010.2f

- %% = 자체 출력

- 용법 "~~~%s %s" %("text", "t2")

- 사용법 2 " %(name)s "%{'name':20}

### str.format 포매팅

- "{0:<10}".format("좌측정렬")

- - < = 정렬 방향, 10 = 문자열 폭

- - <:좌, >:우, ^:중앙

- - 정렬방향앞에 문자를 넣으면 그걸로 공백을 채움

- - ex. {:a<10}

- 숫자도 형식 표기 가능

- - '{:0.2f}'.format(345.14)

- - 위와 같이 하면 소수점 이하 2자 포함 0자리 이지만 정수자리가 지정 자릿수보다 많으면 그냥 출력함

- - 숫자는 앞에 0채우기 밖에 안됨.

### f string

    f법은 print 내부뿐만 아니라 다양한 곳에서 활용 가능

- ```python
  n = int(input())
  print(f'{n:0.2f} inch => {n*2.54:0.2f} cm'
  print(f'{"*"*c:>{b}}')) #갯수 부분에 변수 넣을
  ```

# 3. 변수와 객체

> -  변수: 객체에 대한 식별자 역할

- -  값, 컨테이너, 함수, 클래스가 있다.

```python
# 숫자 a 입력받고 a + aa+ aaa+ aaaa 출력하기
n = input()
print(f"{int(n)+int(n*2)+int(n*3)+int(n*4)}")
```

# 4. 연산자

>  ### 대입연산자, 복합대입연산자

- +,-,*,/,//,%,** 전부 복합대입연산 가능

- (ex. a //= b -> a = a//b)

### 관계연산자

- ==, !=, >,<,>=,<=

### 논리연산자

- and, or , not

### 비트연산자

- &(and), |(or), ^(xor), ~(not), (<< , >> = 좌변 값을 우변값만큼 비트를 방향으로 이동)

### 연산자 우선순위

1. 괄호

2. 산술연산

3. 관계 연산

```python
# inch to cm
n = int(input())
print(f'{n:0.2f} inch => {n*2.54:0.2f} cm')

# kg to lb
n = int(input())
print(f'{n:0.2f} kg =>  {n*2.2046:0.2f} lb')

# celcious to fahrenheit
n = int(input())
print(f'{n:0.2f} ℃ =>  {n*9/5+32:0.2f} ℉')
# fahrenheit to celcius
n = int(input())
print(f'{n:0.2f} ℉ =>  {(n-32)*5/9:0.2f} ℃')

# salt water concentration
print(f'혼합된 소금물의 농도: {(0.2*100)/(100+200)*100:0.2f}%')
```

# 5.흐름제어 (if, elif, else)

**for-else**문은  for가 완전순회하면 else 작동, 중간에 끊기면 작동 x (가끔 쓸만함)

```python
#약수 출력하기
n = int(input())
count = 0
nums = [False] + [True]*n
for i in range(1,n+1):
  if n%i == 0:
    print(f'{i}(은)는 {n}의 약수입니다.')
    count += 1
if count == 2:
    print

#약수 출력 + 소수 판단
n = int(input())
count = 0
nums = [False] + [True]*n
for i in range(1,n+1):
  if n%i == 0:
    print(f'{i}(은)는 {n}의 약수입니다.')
    count += 1
if count == 2:
  print(f'{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.') 


#대소문자 판
t = input()
if t.islower():
  print(f'{t} 는 소문자 입니다.')
elif t.isupper():
  print(f'{t} 는 대문자 입니다.')

#가위바위보 결과 출력.
rcp = dict({"가위":"보","바위":"가위","보":"바위"})
Man1,Man2 = input(),input()
if Man1 == Man2:
  print(f'Result : Draw')
elif rcp[Man1] == Man2:
  print(f'Result : Man1 Win!')
else:
  print(f'Result : Man2 Win!') 

#대소문자 교체 후 아스기 코드도 같이 출력 (전 - 후) 
c = input()
if c.islower():
  print(f'{c}(ASCII: {ord(c)}) => {c.upper()}(ASCII: {ord(c.upper())})')
elif c.isupper():
  print(f'{c}(ASCII: {ord(c)}) => {c.lower()}(ASCII: {ord(c.lower())})') 

#a의 배수이면서 b의 배수는 아닌 수 출력 ,1~200사이
a,b = 7,5
nums = [False] + [False]*200
for i in range(7,201,7):
  if i%a == 0:
    nums[i] = True
for i in range(5,201,5):
  if i%5 == 0:
    nums[i] = False
ans = []
for i in range(201):
  if nums[i]:
    ans.append(i)
print(str(ans).replace(" ","")[1:-1]) 

# 200<=n<300 각 자리수 전부 짝수만 출력
temp = []
for i in range(200,300):
  if not(list(filter(lambda x: x%2,map(int,str(i) ) ) )): #다 홀수면 Falsy
    temp.append(i)
print(str(temp).replace(" ","")[1:-1]) 

# 조건별 출력
scores = [88,30,61,55,95]
for i in range(5):
  print(f'{i+1}번 학생은 {scores[i]}점으로 {"합격" if scores[i]>= 60 else "불합격"}입니다.')

#for 문으로 1~100 출력
for i in range(1,101):
  print(i) 

#for 문으로 1~100중 짝수 출력
temp = []
for i in range(1,101):
  if i%2==0:
    temp.append(i)
print(str(temp)[1:-1].replace(",",""))  

#for 문으로 1~100중 홀수 출력
temp = []
for i in range(1,101):
  if i%2==1:
    temp.append(i)
print(str(temp)[1:-1])  

#1부터 100사이의 숫자 중 3의 배수의 총합
temp = 0
for i in range(1,101):
  temp += i if i%3==0 else 0
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {temp}') 

# 아래 숫자중 80 이상 수의 합을 을 while문과 pop으로 구하기
temp = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
ans = 0
while temp:
  if temp[-1] >= 80:
    ans += temp.pop()
  else:
    temp.pop()
print(ans) 

# while문으로 * 찍기:
c = 5
while c:
  print("*"*c)
  c -= 1 

# while문으로 * 찍기2:
c,b = 7,7
while c>0:
  print(f'{"*"*c:>{b}}')
  c -= 2
  b -= 1 

# 숫자 n에서 0~9가 몇번씩 쓰이는지?
n = input()
nd = dict({f'{i}':0 for i in range(10)})
for i in n:
  nd[i] += 1
print(str(list(nd.keys()))[1:-1].replace("'","").replace(",",""))
print(str(list(nd.values()))[1:-1].replace("'","").replace(",","")) 

#for문으로 별찍기
n=5
for i in range(1,n+1):
  print(f'{"*"*i:>5}') 

#10진수를 2진수로
n = int(input())
print(bin(n)[2:]) 
```

# 함수 강의내용

#### !!! 잠깐 꿀팁 반복문에서 enumerate(iterable, stat=n)으로 시작숫자 조정가능

### 함수의 Argument에서 keyward는 항상 뒤로 빼야함.

ex) def gogo(a, x=3):

### * 는 가변인자 (*args)로 여러개를 인자로 받을 수 있다.

함수안에서는 args 로 받음 (* 뒤에 쓴 이름)

### **kwargs 가변 키워드 인자

몇개의 인자를 받을지 모를때,  딕셔너리로 묶어 처리되고 **를 붙여 표현

```python
def go(father,mather, **pets):
    pass

go("아빠","엄마",dog = "개",cat = "고양이")
#함수내부에 kwargs를 안주면 Falsy 처리됨.  
```

### 패킹 = [~~~~] 묶는것, 언패킹 = [----] -> a,b,c,d

```python
a, *rest , e = [1,2,3,4,5]
#-> rest = [2,3,4]


#Zip의 활용길이가 다르면 길이가 짧은쪽 까지.
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
#dict can take list(tuple,tuple, ... )shape input

#list 뒤집기 1행씩을 1열씩으로 바꾸기 가능
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
```

### Reduce 함수 알아보자!

```python
from functools import reduce
a = [1, 2, 3, 4, 5]
reduce(lambda x,y: x+y, a)
reduce(lambda x,y: x+y, a, 100)
```

function, iterable, initializer순으로 입력

### 함수의 범위

> ###### 함수는 코드 내부에 local scope를 생성하며 그 외의 공간인 global scope로 구분

1. global scope: 코드 어디에서든 참조 할 수 있는 공간

2. local scope: 함수가 만든 scope, 함수 내부에서만 참조 가능

3. global varialbe: global scope에서 정의된 변수

4. local variable: local scope에서 정의된 변수

> ###### 변수의 수명주기

1. built-in scope: 파이썬이 실행된 이후부터 영원히 유지 (파이썬 설치부터)

2. global scope: 모듈이 호출된 시점 이후, 혹은 인터프리터가 끝날 때까지 유지

3. local scope: 함수가 호출할 때 생성되고, 함수가 종료될 때까지 유지

> ###### 이름 검색 규칙(Name Resolution) -LEGB룰
> 
> 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장
> 
> 순서는 아래와 같다.

1. local scope (현재 작업중)

2. Enclosed scope (지역 범위 한 단계 위 범위)

3. Global scope (최상단에 위치한 범위)

4. Built-in scope: 모든 것을 담고 있는 범위 ( 정의 안하고 사용 가능 )

함수 내에서는 바깥 scope의 변수를 수정 할 수 없다.

5. **중요!!** 함수 안에 변수 이름이 없으면 점점 바깥것을 찾는다.

> **주의사항**

1. 파라미터는 글로벌로 쓸수 없고, 글로벌 선언전에 글로벌을 쓸수 없다.

2. global은 없는 변수도 새로 만들어서 global로 지정가능

3. nonlocal : global 제외 가장 가까운(둘러싸는) scope의 변수를 연결함.
   
   1. nonlocal에 나열된 이름은 같은 블록내에서 앞에 등장 불가
   
   2. parameter, for loop 대상, class, 함수 로 정의되있으면 안됨
   
   3. global과 달리 이미 존재하는 이름과의 연결만 가능함.

4. 함수내에서만 필요한건 왠만하면 argument로 받아라

5. 상위 스코프 변수 수정은 global 또는 nonlocal 사용

### 재귀함수

최대 재귀깊이는 1000번이고 늘릴수는 있지만 메모리에 stack이 계속 쌓임.

overflow 발생가능, 기본 호출 최대깊이 넘어가면 에러 발생

```python
def fac(x):
  if x == 1:
    return 1
  else:
    return fac(x-1)*x
```

### PIP

```bash
$ pip freeze > requirements.txt #여기에 pip목록 저장. = 박제
$ pip install -r requirments.txt # 박제한 리스틀 install.
```

### 함수의 장점

1. 구조적 프로그래밍이 가능해짐(큰 프로그램 분할)

2. 필요할 때마다 호출 가능

3. 수정이 용이함

#### 함수 설명

1. 순수함수: 결과값 반환 외에 외부에 영향을 주지 않는 함수

2. 함수 호출 시 입력 값을 전달 받기 위한 변수
   
   전달받은 인자의 값에 의해 타입이 결정됨.
   
   선언된 매개변수의 개수만큼 인자 전달 가능

3. 중첩함수의 은닉을 통한 **closer** 라는 개념이 있다.

```python
#회문 판별기
word = input()
if word == word[::-1]:
  print(word)
  print("입력하신 단어는 회문(Palindrome)입니다.")
else:
  print(word)
  print("입력하신 단어는 회문(Palindrome)이 아닙니다.")  

#2명에게 가위바위보 입력받고 함수로 승패결정하기
def rcp(a,b,aa,bb):
  rcps = dict({"가위":"보","바위":"가위","보":"바위"})
  if aa == bb:
    print("비겼습니다.")
  elif bb == rcps[aa]:
    print(f"{aa}가 이겼습니다!")
  else:
    print(f"{bb}가 이겼습니다!")

rcp(input(),input(),input(),input()) 

#소수판별기
n = int(input())
for i in range(2,n):
  if n%i==0:
    print("소수가아닙니다.")
    break
else:
  print("소수입니다.") 

#피보나치수열 생성기
def fibo(n):
  temp = [1,1]
  if n <=2:
    return temp[:n]
  else:
    for i in range(2,n):
      temp.append(temp[i-1]+temp[i-2])
    return temp
n = int(input())
print(fibo(n)) 

#리스트를 유일한 값만 가진 리스트로 반환 함수 만들기
temp = [1,2,3,4,3,2,1]
def no_ovl(x):
  return list(set(x))
print(temp)
print(no_ovl(temp)) 

#정렬된 숫자 리스트에서 숫자찾기 함수
def nfind(xlist,*n):
  print(xlist)
  ans = []
  for i in n:
    ans.append(True if i in xlist else False)
    print(f'{i} => {ans[-1]}')
  return list(zip(n,ans))
a = [2,4,6,8,10]
nfind(a,5,10) 

#n! 함수 만들기
def fac(x):
  if x == 1:
    return 1
  else:
    return x*fac(x-1)
n=int(input())
print(fac(n)) 

# 제곱함수 만들기
def sq(n):
  n = list(n)
  n.sort()
  ans = []
  for i in n:
    ans.append(i**2)
    print(f'square({i}) => {ans[-1]}')
  return ans
sq(map(int,set(input().replace(",","").replace(" ","")))) 

# 입력된 두 문자열 중 더 긴 문자열 출력
def longer(a,b): # 같을 경우 없을떄
  print(a) if len(a)>len(b) else print(b)
a,b=input().replace(" ","").split(",")
longer(a,b) 

# n부터 카운트다운하는 함수
def countdown(n):
  print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
  if n<1:
    return None
  for i in range(n,0,-1):
    print(i)
countdown(int(input())) 

```

## Wappalizer 라는 웹 분석기 있음

### 가상환경 만들기

```bash
$python -m venv 폴더명
$python -m venv venv 처
```

## 내장함수

`divmod(a,b)` 몫과 나머지 반환 a//b, a%b

`all(iteralbe)` iterable을 넣으면 모두 True면 True 아니면 False 반환 = AND

`any(iteralbe)` iterable을 넣으면 모두False면 False 아니면 True 반환 = OR

`filter(함수,iterable)` 함수 적용결과가 true것만 반환

`sorted()`는 정렬된 리스트를 반환/ 반면 list.sort()는 list를 정렬하고 None값 반환

`reversed()`도 위와 유사하다.

`zip (*args)` iterable 들 중 동일 위치의 항목을 tuple로 묶어 zip 객체 생성

`chr()` 유니코드 문자로, `ord()` 유니코드 값으로, `hex()` 16진수로

`dir(객체)` -> 객체가 가진 변수, 메서드와 같은 속성 정보를 리스트로 반환

    + 인자가 없으면 현재 지역 스코프에 대한 정보를 리스트 객체로 반환

`globals()` 현재 전역 심볼 테이블을 보여주는 딕셔너리를 반환

    +(전역변수와 함수, 클래스 정보 포함)

`locals()` 현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환

    + 매개변수를 포함한 지역변수와 중첩함수의 정보 포함.

`id()` 인자로 전달된 객체의 고유주소를 반환

`isinstance(a,b)` 객체 a가 class b의 instance (생산품,사례) 인지 반환

`issubclass(a,b)` class a가 class b의 subclass인지 반환

`eval()` 실행 가능한 표현식의 문자열을 인자로 전달받아 해당 문자열의 표현식을 실행한

    결과값을 반환

```python
g = dict(globals()) #locals 도 이렇게 확인가능
for item in g.items(): 
  print("\t{0} : {1}".format(item[0],item[1]))
```

```python
#가변형인자로 정수 입력받고 그 곱 반환
#인자의 문제로 에러가 생기면 예외처리
def mul(*n):
  ans = 1
  disc = 0
  for i in n:
    try:
      disc += i
      ans *= i
    except:
      print("에러발생")
      return None
  return ans
mul(1,2,'4',3) 

#주어진 문자열에 쓰인 문자별 점수 총합구하기
#map, lambda 사용
t_sc = dict({"A":4,"B":3,"C":2,"D":1})
text= "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
temp = map(lambda x: t_sc[x] ,list(text))
print(sum(temp)) 

#이름과 나이 입력받고 올해를 기준으로 특정 나이가 되는 해
import time
year = int(time.ctime()[-4:])
name = input()
old = int(input())
target_old = 100
print(f'{name}(은)는 {target_old-old+year}년에 100세가 될 것입니다.') #이게 정답 

#아스키 코드 값을 입력받아 문자로 변환
n = int(input())
print(f'ASCII {n} => {n:c}') 

#filter와 lambda로 1~n중 짝수만 리스트반환
n = 10
nums = list(filter(lambda x: x%2 ==0 ,range(1,n+1)))
print(nums) 

#map과 lambda로 1~n의 제곱값 리스트 반환
n = 10
nums = list(map(lambda x: x**2 ,range(1,n+1)))
print(nums)

#map,filter,lambda로 1~n중 짝수의 제곱값 리스트 반환
n = 10
nums = list(filter(lambda x: x%2==0,map(lambda x: x**2 ,range(1,n+1)) ))
print(nums) 

#가변 인자 받아 max값 return 함수 정의
def max(*nums):
  temp = nums[0]
  for i in nums:
    temp = i if temp < i else temp
  print(f'max{nums} => {temp}')
  return temp
max(3, 5, 4, 1, 8, 10, 2) 

# 문자열의 각 문자를 키로하고 0~n사이 정수를 값으로 하는 딕셔너리 생성
# 이 딕셔너리의 키, 값 출력
n=5
text = 'abcdef'
nums = range(n+1)
ans = dict(zip(text,nums))
for i in ans.keys():
  print(f'{i}: {ans[i]}')


```

## 구문오류와 예외(exception) -> both error

- **구문오류**:잘못된 명령 발생시 구문오류 발생

- **예외**: 문법적인 문제는 없는데 실행 중에 예기치 않게 발생함

#### <예외 발생시 해결 방법>

1. if 문을 이용한 예외의 처리 ( 정상적인 흐름을 제어할 경우에만 가능)
   
   - 예외를 사전에 차단

2.  try except 문
   
   - 예외가 발생했을 때 처리

3. try except else문
   
   - 예외가 발생했을 때 처리 (except)
   
   - 예외가 발생하지 않았을떄 (else = try 정상 시행시 이어서)

4. try except else finally문
   
   - 예외가 발생했을 때 처리
   
   - 예외가 발생하지 않았을떄
   
   - 예외 발생과 상관없이 (finally = 예외 발생하든 말든 그 다음에 실행)

#### 예외 객체

코드 실행 중 오류가 발생하면 만들어진 것, 오류 발생과 관련한 정보를 가짐

```python
try:
    ~~~
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)
# don't have to part "as ~" it's just renaming error
```

- `raise`문을 이용한 강제 예외 발생도 가능

- ```python
  if a < 1 or a > 5:
      raise ValueError
  
  if a < 1 or a > 5:
      raise Exception("에러에러에러!!")
  
  try 안에서 raise 발생시켜서 except 로 넘길수도 있다!
  
  
  ```
