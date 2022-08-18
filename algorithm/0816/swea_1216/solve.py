import sys
sys.stdin = open('input.txt',encoding='utf-8')
def is_pal(x):
    if len(x) < 2: return True
    elif x[0] != x[-1]: return False
    else: return is_pal(x[1:-1])
def is_pal(x): #이게 재귀보다 조금 더 빠름
    for i in range(len(x)):
        if x[i] != x[-i-1]:
            return False
    else: return True
for t in range(1,11):
    tc = int(input())
    text = [input() for i in range(100)]
    ttext = list(zip(*text))
    maxv = 0
    for z in range(100):
        l = 100
        for i in range(100-maxv): # 0 ~ 100
            if l-i < maxv:
                break
            m1 = False
            for k in range(i+1): # 0 ~ i+1
                if m1:
                    break
                if text[z][k] == text[z][k+l-i-1]:
                    if is_pal(text[z][k:k+l-i]):#범위는 i ~ 100 -  i
                        maxv = l - i
                        m1 = True
                        break

    for z in range(100):
        l = 100
        for i in range(100-maxv): # 0 ~ 100
            if l-i < maxv:
                break
            m2 = False
            for k in range(i+1): # 0 ~ i+1
                if m2:
                    break
                if ttext[z][k] == ttext[z][k+l-i-1]:
                    if is_pal(ttext[z][k:k + l - i]):  # 범위는 i ~ 100 -  i
                        maxv = l - i
                        m2 = True
                        break #1줄의 max 찾으면 종료

    print(f'#{t} {maxv}')



# def rowf(x,l):
#     for i in range(100): #전부다 확인은 하긴 해야함. 1~100줄까지
#         for j in range(100-l+1):
#             end = j + l - 1 # indexing 용
#             for k in range(l >> 1):#2로 나눔
#                 if x[i][j+k] != x[i][end-k]: #양끝에서 다가오며 확인
#                     break
#             else:
#                 return l
#     return 1
#
# def colf(x,l):
#     for i in range(100): #전부다 확인은 하긴 해야함. 1~100줄까지
#         for j in range(100-l+1):
#             end = j + l - 1 # indexing 용
#             for k in range(l >> 1):#2로 나눔
#                 if x[i][j+k] != x[end-k][i]: #양끝에서 다가오며 확인
#                     break
#             else:
#                 return l
#     return 1


# #다른 빠른 코드
# def find(arr, l):
#     for rc in range(100):
#         for s in range(100 - l + 1):
#             e = s + l - 1
#             for i in range(l >> 1):
#                 if arr[rc][s + i] != arr[rc][e - i]: break
#             else:
#                 return l
#     return 1
#
#
# def find2(arr, l):
#     for rc in range(100):
#         for s in range(100 - l + 1):
#             e = s + l - 1
#             for i in range(l >> 1):
#                 if arr[s + i][rc] != arr[e - i][rc]: break
#             else:
#                 return l
#     return 1
#
#
# for tc in range(1, 11):
#     N = int(input())
#     arr = [input() for _ in range(100)]
#     ans = 1
#     l = 2
#     while l <= 100 and l <= ans + 2:
#         if ans < find(arr, l):
#             ans = l
#         l += 1
#     l = ans + 1
#     while l <= 100 and l <= ans + 2:
#         if ans < find2(arr, l):
#             ans = l
#         l += 1
#
#     print('#{} {}'.format(tc, ans))