import sys
# sys.stdin = open('input.txt')
"""
2xn 타일링
1x2, 2x1, 2x2 타일로 채우는 방법의 수
   1x2, 2x1, 2x2
1 : 0,   1 ,  0
p2 : 1,   1 ,  1
# 1개를 추가하는 방법은 1개
# 2개를 추가하는 방법은 2개
p2*a + b
"""
# n = int(input())
# a,b = 1, 3
# ans = 0
# if n == 1 : ans = a
# elif n == p2: ans = b
# else:
#     for i in range(3,n+1):
#         ans = p2*a + b
#         a,b = b,ans
# print(ans%10007) # 출력 양식 확인

#속도 올리기
#채점방식이 특이해서 속도차이 안나는 듯
arr = [0,1,3]+[0]*998
for i in range(3,1001):
    arr[i] = (2*arr[i-2] + arr[i-1])%10007
if __name__=="__main__":
    print(*map(lambda x:arr[int(x)],open('input.txt')),sep='\n')
