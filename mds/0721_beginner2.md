# Beginner 2

## 1.  표준모듈과 활용

`import ~~ as ~~`

`from ~~ import ~~` 에서 `import *`은 전부 불러오기

## 2.  표쥰 모듈 종류

1. `sys`

2. `random`
   
   1. `uniform` , `randrange` , `choice`, `choices`, `sample`, `shuffle`

3. `datetime`
   
   1. `datetime.now()` =  현재 지역의 날짜와 시각정보를 가진  datetime객체 반환 
      
      1. ```python
         from datetime import datetime #동작 서버상 시가.
         now = datetime.now()
         print("{0}-{1:02}-{2:02} {3:02}: {4:02} : {5:02}".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
         fmt = "%Y{0} %m{1} %d{2} %H{3} %M{4} %S{5}"
         print(now.strftime(fmt).format(*"년월일시분초")) 
         ```
   
   2. `timezone`,
   
   3. `timetable`

## 3. 서드파티모듈

    1.  `pytz`라는 시간 모듈 있음. 

## 4. 사용자정의 모듈

> 1. **모듈의  `__name__`  속성**
>    
>    1. 실행 목적의 모듈
>       
>       - `__ name__`속성에 `"__main__"` 문자열 값이 들어가 있음
>    
>    2. 라이브러리 목적의 모듈
>       
>       - `"__main__"` 속성에 모듈의 이름이 저장되어 있음

## 5. 사용자 정의 패키지

- 모듈이 모여서 패키지를 정의할 수 있다.
1. 먼저 폴더를 생성한다.

2. 폴더안에  module.py 파일들을 넣는다.

3. `__init__.py` 파일을 만들어  아래와 같이 작성
   
   사실 3.6x 이상 버전부터는 `__init__.py`파일이 없어도 패키지로 인식함.
   
   ```python
   __all__ = ["module1","module2"] #save module names at __all__ attibute
   print("package_mymodul을 로딩하였습니)
   ```

### <잠깐 팁>

1. `zip(*iterable)`은 **Transpose**에 용이함)

## 6. list 다루기

1. `list.insert(index, item)` 으로 지정 위치에 값 끼워넣기 가능

2. `list.extend(list)` 는 list 확장

3. `list.append(item)` 는 값 추가

4. `del list[index]` 인덱스에 해당하는 값 제거 , 슬라이싱도 가능

5. `list.pop(index = -1)` 기본적으로 마지막 값 뽑고 반환, index 지정 가능

6. `list.remove(item)` item 값을 가진 첫번째 값을 제거

7. `list.clear()` list 전체 초기화해서 [] 반환
   
   - `del list[:]`도 같은 기능

8. ` item in list`로 item 이 list 에 있는지 확인, 또는 not in

9. ` list.count(item)` list 에 item이 몇개 있는지 확인

10. `list = [~ for i in data if ~] ` 까지만 써도 list 내포가 됨
    
    - 조건식은 ` a = ~ if ~ else ~` 처럼 else까지 써줘야함.

11. **` "구분자".join(iterable)` = list를 구분자 기준 str로 합쳐준다.**

## 7. tuple 다루기

1. index 접근 가능/ 값 변경 불가

2. `tuple3 = tuple1 + tuple2` 와 같은 덧셈연산 가능

3. `tuple*3` 과 같이 list나 string 처럼 곱하기 가능

4. `item in tuple` list 처럼 사용 가능, 또는 not in

5. tuple도 list처럼 내포가 있음.

```python
# 점수 tuple 저장된 요소를 가진 list 있다.
# 단순 출력하기
scores = [(90,80),(85,75),(90,100)]
for i in range(len(scores)):
  print(f'{i+1}번 학생의 총점은 {sum(scores[i])}점이고, 평균은 {sum(scores[i])/2:0.1f}입니다.') 

#모음 제거기 list 내포 사용
text = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
temp = [i for i in text if i not in 'aeiou']
print(''.join(temp)) 

#2~9단까지 구구단 결과중 3 또는 7의배수를 제외한 리스트 각 단별로 삽입후 출력
ans = []
for i in range(2,10):
  dan = []
  for k in range(1,10):
    if (i*k%3==0 or i*k%7==0):
      pass
    else:
      dan.append(i*k)
  ans.append(dan)
print(ans) 

#입력된 값의 평균 출력
nums = [int(input()) for i in range(5)]
print(f'입력된 값 {nums}의 평균은 {sum(nums)/5}입니다.') 

# n 입력시 약수 리스트 출력
temp = []
n = int(input())
for i in range(1,n+1):
  if n%i==0:
    temp.append(i)
print(temp) 

# n 입력시 약수 리스트 출력 by 리스트 내포
n = int(input())
temp = [i for i in range(1,n+1) if n%i==0]
print(temp) 

#리스트가 주어질 때 그중 짝수만 가진 list 반환
temp = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
temp = list(filter(lambda x: x%2==0,temp))
print(temp) 

#피보나치 수열 10번째 까지 출력
temp = [1,1]
for i in range(2,10):
  temp.append(temp[i-1]+temp[i-2])
print(temp) 

#list 내포로 1~n까지 수중 3또는 5의 배수가 아닌 숫자들의 제곱값 리스트 출력
temp = [i**2 for i in range(1,21) if (i%3!=0 or i%5!=0)]
print(temp) 

#숫자입력의 각 자릿수의 합 반환
n = input()
def nsum(n):
  return sum(map(int,set(n)))
print(nsum(n)) 

#입력 받은 문자열 리스트를 가나다 순으로 따로 묶어서 리스트 내포이용 반환
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),
               ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
                   '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
                   '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
temp = [[i for i in inputWord if ord(i[0])<= ord(k[1]) and ord(i[0])>= ord(k[0])]  for k in dicBase]
print(temp) 

# , 구분 값을 받아 리스트, 튜플 반환
n = list(map(int,input().split(","))) #map은 한 번 사용하면 사라짐. 주의!
print(n)
print(tuple(n))

# , 구분 값을 받아 이들에 대한 원주 길이 계산
n = list(map(lambda x: round(int(x)*3.141592*2,2),input().split(",")))
print(str(n)[1:-1]) 

# 행,열 길이 입력받고 2d matrix 생성, 초기값 = 행 index * 열 index
a,b = map(int,input().split(","))
ans = []
for i in range(a):#행
  temp = []
  for k in range(b):#열
    temp.append(i*k)
  ans.append(temp)
print(ans) 

# ,구분 입력 word를 사전순 정렬하여 출력
words = input().replace(" ","").split(",")
words.sort()
print(str(words).replace("'","")[1:-1]) 

# ,구분 숫자입력 홀수를 ,구분 출력
nums = map(int,input().split(","))
nums = list(filter(lambda x: x%2==1, nums))
print(str(nums)[1:-1]) 

# 입력 튜플을 반으로 갈라 앞뒤 각각 출력
temp = (1,2,3,4,5,6,7,8,9,10)
print(temp[:5])
print(temp[5::]) 

#list 내포로 짝수 제거한 리스트 출력
temp = [5, 6, 77, 45, 22, 12, 24]
temp = [i for i in temp if i%2==1]
print(temp) 

#list 내포로 홀수 번째 항 제거한 리스트 출력
temp = [12, 24, 35, 70, 88, 120, 155]
temp = [temp[i] for i in range(len(temp)) if i%2==1]
print(temp)  


# 2x3x4 shape 0 matrix 출력
print([[[0]*4]*3]*2) #shape 역순으로 곱하면 됨.
# 이렇게 되면 주소를 복사해서 값이 한번에 바뀜. (deep copy) 

#리스트내포활용 특정순번 아이템 제거후 출력
temp = [12, 24, 35, 70, 88, 120, 155]
spe = [1,5,6]
temp = [temp[i] for i in range(len(temp)) if (i+1) not in spe]
print(temp) 

#두 리스트중 둘다 들어있는 값 리스트로 반환
a = [1,3,6,78,35,55]
b = [12,24,35,24,88,120,155]
print(list(set(a).intersection(set(b)) )) 

#리스트 중복제거함수 이용 중복제거한 값 출력
def no_ovl(x):
  return sorted(list(set(x)))
temp = [12,24,35,24,88,120,155,88,120,155]
print(no_ovl(temp)) 
```

# 7. Set 다루기

`{e1, e2, e3}` 또는 `set(iterable)` 의 방법으로 생성

1. ` .union() , .intersection, .difference` 의 집합 연산 메소드있음

2. `A|B, A&B, A-B, A^B` 가 있다. 순서대로 위와 같음 마지막은
   
   - 교집합 제외한 나머지

3. `{}`만쓰면 빈 dictionary가 만들어지므로 빈 셋은 set()  으로

4. `remove(key)` `pop()` pop 은 argument없이 첫 key가 뽑힌다.

5. `clear()` method 사용 가능

6. `in` 으로 특정 원소 포함여부 확인 가능

7. `A.issuperset(B)`로 A가 B전체를 포함하는 확인 가능

8. 위 7번의 반대는 `B.issubset(A)` B가 A에 포함되는가?

9. set 도 내포사용가능 **iterable**은 해당 리터럴 안에서 다된다.

## 8.  Dictionary 다루기

인덱스 x, 순서 x, 중복 x

1. `{a:b, c:d}` 와 같이 생성

2. `dict( 홍길동 =20, 이순신 = 30 )` 으로도 생성 가능하나

        key 부분은 문자열로 쓰면 안됨. (**args 인자 느낌)

    3. `dict.update(~)` 로 요소 추가 가능

        `dict[key] = Value`로도 입력 가능하지만 key가 중복이면

        Value가 교체됨.

4. `del dict(key); dict.pop(key)`로 key 에 맞는 요소 삭제 가능

5. `clear()`도 사용가능

6. `in, not in` 사용 가능

7. `dict.items() ; dict.values(); dict.keys()` 등이 있다.

8. `dict의 내포`
   
   - ```python
     ds = {key:value for key in temp}
     ds = {item for item in dicts.items()}
     ```

9. dict() 안에 iterable composed by tuple(a,b) it can be dict

```python
#전화번호부 프로그램
phone = dict(홍길동= '010-1111-1111',이순신= '010-1111-2222',강감찬= '010-1111-3333')
print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for i in phone.keys():
  print(i)
name = input("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.\n")
print(f'{name}의 전화번호는 {phone[name]}입니다.')  

#dict 가격따라 내림차순 정렬
furniture = dict({"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000})
temp = []
for i in furniture.items():
  temp.append(i)
temp.sort(key= lambda x:x[1],reverse=True)
for i in temp:
  print(str(i).replace(",",":").replace("'","")[1:-1]) 

# recursive
def is_pal_recursive(word):
    if len(word) < 2: #글자길이 2까지 같은걸 확인후 재귀시 True 반환
        return True   #홀수길이면 1
    if word[0] != word[-1]: #길이 2까진 word 의 첫글자 마지막 글자 확인
        return False        #홀수길이면 3
    return is_pal_recursive(word[1:-1]) # 양 끝씩 잘라가며 재귀  

#두 딕셔너리 합치고 3000원 이상인 메뉴 출력
#중복이 있다면 a 정보 따르기
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
b.update(a)
temp = []
for i in b.items():
  if i[1] > 3000:
    temp.append(i)
print("{"+f'{str(temp)[1:-1]}'+"}")  

#리스트 원소를 key, 그 length를 value로하는 dict 생성
fruit = ['   apple    ','banana','  melon']
fdict = {i.strip():len(i.strip()) for i in fruit}
print(fdict) 

#n입력 받고 1~n = key 그 제곱은 value로하는 dict
ndict = {i:i**2 for i in range(1,int(input())+1)}
print(ndict) 

#input text중 숫자 문자(알파벳만) 구별해 각각 개수 출력
text = input()
info = {'LETTERS':0, 'DIGITS':0}
for i in text:
  if i.isnumeric():
    info['DIGITS'] += 1
  elif i.isalpha():
    info['LETTERS'] += 1
print(f"LETTERS {info['LETTERS']}")
print(f"DIGITS {info['DIGITS']}") 

#input text 에서 대소문자 구별 각각 갯수 출력
text = input()
u,l = 0,0
for i in text:
  if i.islower():
    l+=1
  elif i.isupper():
    u+=1
print(f"UPPER CASE {u}")
print(f'LOWER CASE {l}') 

#기존가격 인상하기 by dict 내포
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beer_after = {key:beer[key]*1.05 for key in beer.keys()}
# dict(sorted(beer.items(),key = lambda x:x[1])) 이렇게 순서 뒤집기 가능
print(beer)
print(beer_after) 

#입력된 text의 문자 빈도수 출력
text = input()
tdict = {i:0 for i in text}
for i in text:
  tdict[i]+=1
for i in tdict.items(): 
  print(i[0],",",i[1],sep="") 
```

## 9. 문자열 연산

1. `+`로 문자열 연결해 새로운 문자열 생성 가능

2. `*` 문자열 반복 연산자

3. 다른 iterable 처럼 index로 값 참조 가능, 수정은 불가.

4. `문자열[시작:끝:간격]` slicing 가능
- 문자열 함수
  
  1. `count(문자), len(문자열)` 사용가능
  
  2. `문자열.find(찾을 문자열) ;문자열.rfind(찾을 문자열)`
     
     1. find는 찾으면 그 시작 index 반환, 못찾으면 -1 반환(L to R)
     
     2. rfind는 위와 같지만 탐색을 오른쪽에서 왼쪽으로(R to L)
     
     3. `문자열.index(문자열)` 은 못찾으면 ValueError 발생
  
  3. `(구분자).join(iterable)` 은 iterable의 각 원소 사이에
     
     구분자를 끼워넣어서 문자열 생성
  
  4. ` str.capitalize() = 첫 문자를 대문자로`
     
     `.upper() = 모두 대문자로, .lower() = 모두 소문자로`
  
  5. 공백제거 (셋다 넣어준 인자가 안나타날때 까지만 제거)
     
     1. `.lstrip(" ")` 인자로 전달된 문자를 왼쪽부터 제거
     
     2. `.rstrip("_ ")` 오른쪽에서 부터 에서
     
     3. `.strip(" ")`은 양끝에서 시작
  
  6. `문자열.replace("교체하고싶은 문자","교체할 문자")` 로 교체 가능
  
  7. `.split("구분자")`  구분자를 기준으로 문자열을 구분해 list 반환 

```python
#paindrome 판단하기 slicing,for, while 다 가능
#그냥 재귀로 연습
def is_pal(x):
  if len(x)<2:
    return True
  if x[0] != x[-1]:
    return False
  else:
    return is_pal(x[1:-1])
word = input()
if is_pal(word):
  print(word)
  print("입력하신 단어는 회문(Palindrome)입니다.")
else:
  print(word) 
  print("입력하신 단어는 회문(Palindrome)이 아닙니다.") 

#입력 구성 단어를 역출력하기
text = input().split(" ")
text.reverse()
print(" ".join(text)) 

#URL 받아서 프로토콜,호스트, 나머지 구분하기
url = input()
pr = url.find("://")
host = url[pr+3:].find("/") + pr + 3 
print(f'protocol: {url[:pr]}')
print(f'host: {url[pr+3:host]}')
print(f'others: {url[host+1::]}')

#여러 sentence 받고 대문자로 반환
#enter만 입력시 종료
#swexpertacademy.com 입력이 enter를 똑바로 안넣음.. 그래서 코드수정
ss = []#3번만 입력함
while 1:
  if len(ss) == 3: 
    break
  else:
    ss.append(input())
for i in ss:
  print(f'>> {i.upper()}') 

# 입력은 공백(space) 구분
# 중복단어 없이 단어를 콤마로 구분 사전순 출력
text = list(set(input().split(" ")))
text.sort()
text = ",".join(text)
print(text) 

#문자열을 입력하면 짝수 index만 출력
text = input()
print(text[0::2]) 
```

## 10. 객체 지향의 이해 (Object Oriented)

대규모 프로그램 효율적 코딩 가능

- Object Oriented Programming (객체지향 프로그래밍)
  
  1. 객체 형성(상태와 행위로 이루어짐)
  
  2. 객체 조립
  
  3. 프로그램 형성
  
  4. = 객체를 이용해 문제를 해결하려는 프로그래밍 방법

- 객체란? **변수(값)와 메서드(실행 코드)를 하나로 묶은 것!** 
  
  - ex) 자동차의 변수: 연료량, 속도계
  
  - 자동차의 메서드: 주행기능
  
  - 이처럼 변수와 연관된 기능을 메서드 라고한다.
  
  - 서로 연관된 변수와 메서드를 잘 파악하고
  
  - 묶어 객체를 형성하는 것이 중요!
  
  - 부품화와 재사용성이 뛰어남.

- 객체 지향의 구성요소 : 클래스, 변수. 메서드

- 용어
  
  1. 클래스: 부품 객체를 만들기 위한 청사진, 설계도, 템플릿
     
     1. 같은 문제 도메인에 속하는 속성(att)과 행위를 정의
     
     2. OOP의  기본적인 사용자 정의 data type
  
  2. 객체(object)
     
     1. 메모리에 로딩된 클래스를 통해 클래스를 템플릿으로
        
        하여 메모리 상에 생성된 정보 = 인스턴스(Instance)
     
     2. 자신의 고유의 속성을 가지며 클래스에서 정의한 행위 수행
     
     3. 객체의 행위는 클래스에서 정의된 행위에 대한 정의를 공유함으로써
        
        메모리를 효율적으로 사용
  
  3. 메서드(method)
     
     1. 메시지(message)라고도 부름
     
     2. 클래스로부터 생성된 객체 사용 시 객체에 명령을 내리는 행위
        
        - 객체가 가지고 있는 메서드를 호출한다.
        
        - 객체에 메시지를 전달한다.
     
     3. 한 객체의 속성을 조작할 목적으로 사용
     
     4. 객체 간의 통신은 메시지 전달을 통해 이루어짐

- #### 특징
  
  1. 추상화 : 객체에서 공통된 속성과 행위를 추출하는 것
     
     - 공통의 속성과 행위를 찾아서 타입을 정의하는 과정
     
     - 이를 통해 만든 데이터 타입을 만들 수 있다.
       
       1. 데이터 타입의 표현과 연산을 캡슐화
       
       2. 접근 제어를 통해 데이터의 정보를 은닉 가능
       
       3. 추상 데이터 타입 = class(클래스)
       
       4. (3)의 인스턴스는 = object(객체)
       
       5. (3)에서 정의된 연산 = method(메서드)
  
  2. 상속: 새로운 클래스가 기존 클래스의 데이터와 연산 사용가능하게 함.
     
     1. 기존: 부모, 기반. 상위, 슈퍼 ↓
     
     2. New: 자식, 파생, 하위, 서브
     
     3. 하위 클래스를 이용해 프로그램 요구에 마주어 클래스 수정 가능
     
     4. 파이썬은 단일 상속만 지원한다.
     
     5. 상속받은 부모클래스의 method나 변수 호출시
        
        그냥 클래스 안에서 `부모클래스명.변수`같이 꺼내면 됨
        
        또는 `super().변수`
     
     6. 클래스 간의 종속 관계를 형성하여 객체 조직화
     - 상속의 장점
       
       1. 재사용으로 인해 코드가 줄어듦
       
       2. 범용적인 사용 가능
          
          (ex. object type 매개변수에 string, int 객체 사용가능)
          
          (둘다 object 상속을 받기 때문)
       
       3. 자료와 메서드의 자유로운 사용 및 추가 가능
  
  3. 다형성: 어떠한 요소에 여러 개념을 넣어 놓는 것
     
     - 오버라이딩: 같은 이름의 메서드가 여러 클래스에서 다른기능을 하는 것.
       
       - 메서드 오버라이딩: 상속으로 물려 받은 자료나 메서드를 그대로 쓰지 않고 
         
         하위 클래스에서 새로 정의해 사용하는 기법 = **덮어쓰기**
         
         1. 상위 클래스의 메서드와 동일한 서명
            
            (매개변수의 타입, 개수, 리턴 타입)을 가져야함.
            
            -> 코드의 재사용성 향상
     
     - 오버로딩: 같은 이름의 메서드가 인자의 개수나 자료형에 다라서 
       
       다른 기능을 하는 것
       
       - 메서드 오버로딩: 클래스 내부에 동일한 이름의 행위를 여러개 정의하는 것
         
         1. 메서드의 이름이 같고, 매개변수의 타입과 수는 서로 달라야 함
         
         2. 리턴 타입은 관계하지 않음
         
         3. 메서드 이름을 하나로 통일 가능하며, 같은 이름의 메서드에
            
            여러 종류의 매개 변수를 받을 수 있음.

- **클래스 정의** = `class 클래스명:` 으로 정의
  
  - 객체 공간의 필드와 메서드에 접근시 `self.식별자`  이용
  
  - `def __init__(self, 매개변수목록):` 생성자 메서드 정의
  
  - `def __del__(self):`소멸자 메서드 정의 (self 만 인자로 받음)

- 객체 생성 = 클래스명() -> 생성자 메서드 = 클래스 이름과 동일한 메서드
  
  - `isistance(객체, class)` 를 통해 클래스의 인스턴스 여부 확인
  
  - 인스턴스 메서드(instance method)
    
    self가 가리키는 객체의 필드 정보에 접근해 특정 목적의 기능을 수행하도로
    
    정의된 메서드 (self.method)
  
  - 인스턴수 변수(instance variable) = self.변수 형태의 변수
    
    값이 막 바뀔 수 있기 때문에 값 접근 제한 필요
    
    `self.__name = name` 과 같이 `__`를 붙여서 프라이빗 필드 생성
    
    이 때 접근하려면 `getter` (읽기), `setter`(변경) method가 필요
    
    특별한 건 아니고 읽고 싶거나 변경하고 싶은것을 return 하는
    
    instance method를 추가로 정의 ex)`get_name(self):`
  
  - **Decorator** 기능
    
    ```python
    class go:
      def __init__(self,name):
        self.__name = name
    
      @property
      def name(self): #변수처럼 사용 가능하며 ,getter method 역할을 한다.
        return self.__name
    
      @name.setter
      def name(self,name):
        if name == "":
          raise TypeError("이름을 지어주세요.")
        self.__name = name
    
    a = go("소")
    print(a.name)
    a.name = "gogo"
    print(a.name)  
    
    class car: # 접근은 클래스명.클래스변수 -> car.count
      count = 0 #클래스 변수
      def __init__(self,year):
        self.year = year
      @classmethod
      def surplus(cls,*a): #cls 라는 클래스 자신에 대한 참조 전달
        pass #사용 방법: 클래스명.클래스메서드(매게변수 목록)
      def __gt__(self,other): #class instance간  > 쓰면 호출됨 
        return self.year > other.year 
      def __ge__(self,other): #아래도 같다.
        return self.year >= other.year
      def __lt__(self,other):
        return self.year < other.year
      def __le__(self,other):
        return self.year <= other.year
      def __eq__(self,other):
        return self.year == other.year    
      def __ne__(self,other):
        return self.year != other.year
    
      def __str()__(self): # str()함수에 객체 전달후 문자열로 변환
        return f'{self.year}년 식 차'  
    #str(객체)를 하면 __str()__ method 호출수
    #__repr__ 등 다양한 method 가 있다.
    ```

- 클래스 변수의 정의 및 접근 ↑

```python
#3개 숫자를 받아 합계 구하기
class score:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
  def __repr__(self):
    return f'국어, 영어, 수학의 총점: {self.a + self.b + self.c}'
st1 = score(*map(int,input().split(",")))  
print(st1)  

class Korean:
  def __init__(self,country):
    self.country = country
    print(country)
  def printNationality(self):
    print(self.country)
a = Korean("대한민국")
a.printNationality()   

class Student:
  def __init__(self,name):
    self.__name = name
  @property
  def name(self):
      return f'{self.__name}'   


#class상
class GraduateStudent(Student):
    def __init__(self,name,major):
        self.__major = major
        super().__init__(name)
    @property
    def major(self):
        return self.__major

a = Student('홍길동')
b = GraduateStudent('이순신','컴퓨터')
print(f'이름: {a.name}')  
print(f'이름: {b.name}, 전공: {b.major}')   

class Circle:
  def __init__(self,rad):
    self.rad = rad
  @property
  def area(self):
    return 3.14*self.rad**2
a = Circle(2)  
print(f'원의 면적: {a.area}')  

class Rectangle:
  def __init__(self,width,length):
    self.width = width
    self.length = length
  @property
  def area(self):
    return f'사각형의 면적: {self.width*self.length}'
a = Rectangle(4,5) 
print(a.area) 
 
class Shape:
  def __init__(self):
    pass
  def area(self):
    return 0
class Square(Shape):
  def __init__(self,length):
    self.length = length
  @property
  def area(self):
    return self.length**2

a = Square(3) 
print(f'정사각형의 면적: {a.area}') 

class Person:
  def __init__(self,gender):
    self.gender = gender
  def getGender(self):
    return "Unknown"

class Male(Person):
  def __init__(self):
    self.gender = "Male"
  @property
  def getGender(self):
    return self.gender

class Female(Person):
  def __init__(self):
    self.gender = "Female"
  @property
  def getGender(self):
    return self.gender

man = Male()
woman = Female()
print(man.getGender)
print(woman.getGender)


```
