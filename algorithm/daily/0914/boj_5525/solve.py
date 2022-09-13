import sys
sys.stdin = open('input.txt')
"""
대문자 o가 n개 (소문자가 아니라 대문자임 ...)
대문자 I가 n+1개
Pn = IOIOI... 이다.
문자열 S와 정수 n이 주어질때 Pn의 개수
"""
n = int(input())
m = int(input())
s = input()
P = 'I'+'OI'*n
#단순히 IOIO가 번갈아 나타나는 구간의 개수만 파악하면 될듯
i = 0
ans = 0
while i < m:
    if s[i] == 'I':
        temp = i
        while 1:
            if i+2 < m and (s[i+1],s[i+2]) == ('O','I'):
                i+=2
            else: break
        count = (i-temp)//2-n+1 # 3, 1
        ans += max(count,0)
    i += 1
print(ans)
#P는 무조건 좌우대칭이지만 기각, oooo도 해당
# def is_pal(x):
#     idx = 0
#     n = len(x)-1
#     if n <=0: return 1
#     while x[idx] == x[n-idx]:
#         idx+=1
#         if idx >= n//2: return 1
# for size in range(m,0,-1):
#     for i in range(m-size+1):
#         if is_pal(s[i:i+size]):


