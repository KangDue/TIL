import sys
sys.stdin = open('input.txt')

"""
리모컨
채널범위 0~무한대
0~9숫자와 + - 버튼
+s는 채널 1 증가, - 는 1 감소
현재채널(100), 고장난 버튼이 주어지고
이동하려는 채널로 몇번 버튼을 눌러야 이동가능한가?
고장난 버튼의 개수는 0~10개

버튼을 누른 횟수 + 가능한 모든 경우의수로 풀었다.
단순히 숫자 자릿수와 그 자릿수만큼 버튼 중복순열로 풀면 무조건 틀린다.
한자리수 위에서 내려온게 빠를수도 있고 한자리수 밑에서 한게 빠를수도 있기 때문이다.
"""
import sys
def pmr(arr,n):
    for i in range(len(arr)):
        if n <= 1: ## ==1 로 하는게 맞고 혹시 <= 로 해버리면 0도 되버려서 이상한 값이 나온다.
            yield [arr[i]] # (음수~0)결과는 1은 n일때와 같은 결과가 나옴.
        else:
            for e in pmr(arr,n-1):
                yield [arr[i]] + e

def cal(x):
    temp=0
    for i in range(len(x)):
        temp += x[i] * 10 ** (len(x) - i - 1)
    return temp

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
if m:
    err = [*map(int,sys.stdin.readline().split())]
else: err=[]
normal = [i for i in range(10) if i not in err]
minv = abs(n-100) #버튼 안눌렀을때
length = len(str(n))+1
pivot = 1 if length <=2 else length - 2
for l in range(pivot,length+1): #0부터 전부 탐색하는거랑 속도가 비슷...
    for i in pmr(normal,l):   # 작은 값들은 경우의수가 어차피 훨씬 적기때문에 큰 영향 없는듯
        temp = cal(i)
        diff2 = abs(n - temp)
        minv = min(minv, diff2 + l)
print(minv)

#가장빠른 숏 코딩.
N=int(input())
M=int(input())
if M:#0이 아니면
    broken=set(input().split())
else:#0이면 빈 공간
    broken=set()
ans=abs(N-100)
for i in range(1000001):#모든 경우의 수
    for j in str(i):
        if j in broken:
            break
    else:
        ans=min(ans,len(str(i))+abs(N-i))
print(ans)