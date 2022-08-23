import sys
sys.stdin = open('input.txt', encoding='utf-8')
a = []
for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort(reverse = True)
    sim = -1
    for i in range(n-1):
        for k in range(i+1,n):
            temp = nums[i]*nums[k]
            if sim > temp:
                break
            temp2 = temp#시작 자릿수
            t1 = temp2 % 10
            temp2 //= 10 #다음 자릿수
            while temp2: # while 도 else 문 있는거 처음 앎..
                t2 = temp2%10
                if t2 > t1:
                    break
                t1 = t2
                temp2 //= 10
            else:
                sim = temp
    a.append(f'#{t} {sim}')
print(*a,sep = '\n')
#
# t = int(input())
# res = []
# for tc in range(t):
#     n = int(input())
#     data = list(map(int, input().split()))
#     data.sort(reverse=True)
#     maax = -1
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             num = data[i] * data[j]
#             if maax > num:
#                 break
#             tmp = num
#             next = tmp % 10
#             tmp //= 10
#             while (tmp):
#                 prev = tmp % 10
#                 if prev > next:
#                     break
#                 next = prev
#                 tmp //= 10
#             else:
#                 maax = num
#     res.append(f'#{tc + 1} {maax}')
#
# for i in res:
#     print(i)
