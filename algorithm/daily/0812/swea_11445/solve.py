import sys

sys.stdin = open('input.txt', encoding='utf-8') #print(f'#{t} Y') print(f'#{t} N')
def check(a,b):#무조건 a가 사전순서가 먼저인 단어임
    if len(a) == len(b):
        if b == a[:-1]+ chr(ord(a[-1])+1): #순서 1개 차이면 중간에 없다.
            print(f'#{t} Y')
        else:
            print(f'#{t} Y')
    else:
        # remain = 'a'*(len(b)-len(a)) #길이 차이 만큼 a 면 aa와 aaaa 사이에 단어가 존재... 장난치냐 ?, 고치니까 99개는 뭔데?
        if b == a+'a': #index 주의 할것
            print(f'#{t} N')# :길이 = 끝을 포함하지 않고, 길이: = 시작을 포함한다.
        else:
            print(f'#{t} Y')

T = int(input())
# for t in range(1,T+1):
#     #알파벳 소문자로 구성된 단어 p,q가 있을때
#     #길이는 1이상 ~ 10이하
#     #사전상에 10자보다 더 긴 단어가 존재 할 수 있다.(진짜 무한 사전)
#     #P는 Q보다 항상 사전상 먼저온다.
#     word = [input().strip() for i in range(p2)] #문제의 input에 공백 장난질이 있다.
#     check(word[0], word[1])

#정말 빡이 치는 규칙이다... 단어사이에 다른 단어가 없으려면 무조건 +'a' 형태여야한다.
# ex) abc와 abb는 그사이가 없어 보이지만
# 무한사전이기에 abca~aaaaa... abcz~zzzzzz 이후 abb이기 때문.
# 따라서 문제가 엄청 간단해진다.
# 김동주씨 코드 참조( 김동주_0829998 )
for t in range(1,T+1):
    if input().strip()+'a' == input().strip():
        print(f'#{t} N')
    else:
        print(f'#{t} Y')