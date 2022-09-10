import sys
sys.stdin = open('input.txt')
# 산술평균,중앙값,최빈값,범위
n = int(input())
info = [0]*8001 # 0~4000, -4000~-1
for i in range(n):
    info[int(input())] += 1
array = []
maxv = max(info)
maxx = []
for i in range(-4000,4000+1):
    if info[i]:
        array.extend([i]*info[i])
        if info[i] == maxv:
            maxx.append(i)
print(int(round(sum(array)/n,0)))
print(array[n//2])
if len(maxx) > 1:
    print(maxx[1])
else:
    print(maxx[0])
print(array[-1]-array[0])