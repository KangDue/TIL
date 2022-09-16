import sys
sys.stdin = open('input.txt')
"""
수 N개가 주어진다.
i~j번째 수까지 합을 구하라.
M회에 걸쳐 i,j 쌍이 주어지고 M회 답을 출력하라.
10만개 배열에서 10만개의 sum 명령 시간이 오래 걸릴듯하니
배열을 만들자.
2차원 배열 만드니까 바로 메모리 초과뜸;(밑에 0인 부분 필요없다.)
dict로 만들자. 이래도 초과뜨네.. 그때그떄 구하는게 원하는것인듯
그때그때 구하니 또 시간초과가 뜨네 ; ? 번뜩
누적합으로 갱신하고 뺄샘을 할까?
식은 군더더기 없어 보이는데 시간이 오래걸리기 한다.(시간초과)
input 받는 시간도 줄여보자
(인풋시간이 문제였음 10만개 정도만 되도 input 받아오는 시간
신경써야 함.)
"""
# n,m = map(int,input().split())
# nums = [*map(int,input().split())]
# for i in range(n-1):
#     nums[i+1] += nums[i]
# for _ in range(m):
#     x,y = map(int,input().split())
#     if x-2 < 0: print(nums[y-1])
#     else: print(nums[y-1] - nums[x-2])

#인풋시간 줄인 버전
o = open('input.txt')
n,m = map(int,next(o).split())
nums = [*map(int,next(o).split())]
for i in range(n-1):
    nums[i+1] += nums[i]
for x,y in map(lambda x:[*map(int,x.split())],o):
    if x-2 < 0: print(nums[y-1])
    else: print(nums[y-1] - nums[x-2])