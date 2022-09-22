import sys
sys.stdin = open('input.txt')
"""
좌표 압축
수직선 위에 n개 좌표 X1~ Xn 이 있다.
압축 결과는 Xi > Xj를 만족하는 서로다른 좌표의 개수와 같아야 한다.
좌표압축을 적용한 결과를 출력하자!
1<=n<=1000000(백만)
-10**9 <= X <= 10**9
#겹치지 않는 다른 좌표의 개수는 정렬했을때 순서와 같다.
"""
input()
data = [*map(int,input().split())]
nums = dict()
for i in data:
    nums[i]=1
for num,con in enumerate(sorted(nums)):
    nums[con]=num
print(*map(lambda x:nums[x],data))

# 1. for문이 으로 list에 담아서 출력하는게 약간 더 빠름
# p2. lamda가 def한 함수를 가져다 쓰는거보다 조금 더 빠름. (map 같은거 에서)
# 3. 이왕 함수를 쓸꺼면 a=~ 같이 변수에 담아서 쓰는게 조금더 빠름 아주조금
# 4. 결국 lambda가 더 빠름
# 5. dict로 값 담아오는게 set보다 중복 없애는 속도가 조금 빠른듯?

