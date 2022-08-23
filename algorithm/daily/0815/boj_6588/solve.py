import sys
sys.stdin = open('input.txt')
limit = 1000000
prime = [False]*3 + [True]*(limit-2)
primes = []
for i in range(3, limit): #홀수 소수만 원함.
    if prime[i]:
        primes.append(i)
    for j in range(2*i, limit, i):
        prime[j] = False
# too much 복사로 갖다놓기는 쫌 ...
pl = len(primes)# 78498
while 1: # b-a를 최대화한 골드바흐 추측 증명해보기
    n = int(sys.stdin.readline())
    if n:
        a,b = 0,0
        find = False
        for i in range(pl): #앞에서 부터 뺀 값이 소수인가? 판별하기 = 바로 성공!
            temp = n-primes[i]
            for j in primes:
                if j == temp:
                    a, b = primes[i], temp
                    find = True
                elif j > temp:
                    break
            if find == True:
                break
        if find:
            print(f'{n} = {a} + {b}')
        else:
            print("Goldbach's conjecture is wrong.")
    else:
        sys.exit() # 0 이면 종료

# try1 시간초과
# while 1: # b-a를 최대화한 골드바흐 추측 증명해보기
#     n = int(sys.stdin.readline())
#     if n:
#         a,b = 0,0
#         find = False
#         for i in range(pl): #앞에서 부터
#             for j in range(i, pl): #i 부터
#                 temp = primes[j]+primes[i] - n
#                 if temp > 0: #양수 되면 바로 종료
#                     break
#                 elif temp == 0:# 0되면 답 발견
#                     a, b = primes[i], primes[j]
#                     find = True
#                     break
#             if find:
#                 break
#         if find:
#             print(f'{n} = {a} + {b}')
#         else:
#             print("Goldbach's conjecture is wrong.")
#     else:
#         sys.exit() # 0 이면 종료