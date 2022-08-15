import sys
sys.stdin = open('input.txt',encoding='utf-8')

# import sys
# def zeromake(arr,n):
#     for z in range(n):  # 상담 못하는 넘들은 0으로 변경
#         if z + arr[z][0] > n:
#             arr[z] = [0, 0]
#     return arr
# n = int(sys.stdin.readline())
# s = [ list(map(int,sys.stdin.readline().split())) for i in range(n)]
# s = zeromake(s,n)
# pos = [s[0][1]]+[0]*(n-1)
# vals = [i[1] for i in s]#값들만 모은 것
# for i in range(1,n):
#     for j in range(i+1,i + s[i][1]):
#         if j < s[i-1][1]: #앞 녀석 범위 안에 존재
#             pos

n = int(input())
s = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
sp = [0 for _ in range(n + 1)]#초기 시작을 위해 0을 하나 더줌.

for i in range(n - 1, -1, -1):
    if i + s[i][0] > n: # 범위 초과 상담이면 0으로 만들기
        sp[i] = sp[i + 1]
    else:
        sp[i] = max(sp[i + 1], s[i][1] + sp[i + s[i][0]])
        #자기 위치에서 최대비용은  -> 뒤의 값 기준 최대비용, 또는 자기 위치 상담비용 + 자기 상담 끝난 날 기준 최대비용
print(sp[0]) # 마지막 날까지 비교후 판단

# for i in range(n-1,-1,-1): #끝에서부터 순회하는게 나아보임.
#     if s[i][1]:
#         for k in range(i+1,i+s[i][0]):
#             if s[i][1] <= s[k][1]:
#                 s[i] = [0,0]
#                 break
#         else:#s[i]가 가장 크면
#             for j in range(i+1,i+s[i][0]): #나머지 0 만들기
#                 s[j] = [0,0]
# vals = [b for a, b in s if b > 0]
# print(sum(vals))