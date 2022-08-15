import sys
sys.stdin = open('input.txt')
T = int(input())
ans = []
for t in range(1,T+1):
#0~100sec light bulb obseve
    secs = list(map(int,input().split()))
    a = [0]*max(secs)
    a[secs[0]:secs[1]] = [1]*(secs[1]-secs[0])
    for i in range(secs[2],secs[3]):
        a[i] += 1
    ans.append(f'#{t} {a.count(2)}')
for i in ans:
    print(i)
#숫자로만 연산해도 되지만 눈에 잘 들어오게 리스트 활용