# 정수 리스트 100만개 크기가 8mb 인데
# 1000만개 정수 받아서 정렬??? 뭐지이거
# 메모리 제한이 8mb 인데 이상하다.
# 다른언어보니 시간제한, 메모리제한 다른데 일단 해본다.
#이렇게 저장하니 바로 메모리 초과뜬다.
# nums = [*map(int,sys.stdin.readlines())]
# nums.sort()
# print(*nums,sep='\n')

#즉, 1줄씩 읽어야한다. 그래서 시간제한도 넉넉한듯. 5초
import sys
sys.stdin = open('input.txt')
ip = sys.stdin.readline
n = int(ip())
info = [0]*10001
for _ in range(n):
    info[int(ip())] += 1
for i in range(10001):
    while info[i]:
        print(i)
        info[i] -= 1
#같은 방법이어도 pypy는 통과 못함.
    # while info[i]:
    #     print(i)
    #     info[i] -= 1
print(9**5)
#숏코딩 참고용
l=[0]*9**5
f=open(0)
next(f) # 이렇게 첫값 넘기기 가능.
for i in f:
    l[int(i)]+=1
for i in range(9**5):
    for j in range(l[i]):
        print(i)

#정말 별의별 방법을 다썻는데 화가난다 ㅠㅠ...
#풀이 찾아보니 나랑 똑같은 풀인데 왜 안되나 했더니
#나는 pypy라 안되고 올린사람은 python이라 되는거였누 ...
#메모리 관리는 pypy보다 python이 효율적이다.
#메모리 제한을 잘보고 값을 1개 1개 처리하는지
#한번에 처리하는지 잘 살펴보자!