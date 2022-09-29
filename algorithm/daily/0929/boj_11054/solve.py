import sys
sys.stdin = open('input.txt')
"""
가장 긴 바이토닉 부분 수열
= 가장 긴 증가하는 부분 수열, 가장 긴 감소하는 부분 수열 각
구간을 나누고 각 구간에 대한 가장긴 증가 부분 수열, 가장 긴 감소 부분 수열 길이의 합
중에서 max? 하면 될라나.
70%
99 % cut
드디어 컷.. 이상한 예외처리 할 생각 말고 첨부터 잘 쌓아올리자
edge case 확인
1) 1 2 3 2 1
2) 1 2 1 2 1
3) 3 2 1
4) 1 1 1
5) 1 2
6) 2 1
7) 1
8) 4 3 2 1 2 3 4 2 1

# 나는 직접 수열을 생성해가는 방식으로 했지만 사실
dp table을 만들어 위치별 최대 개수만 카운팅하면서 합쳐도 된다. (훨 빠름)
"""
import sys
from bisect import bisect_left as bl
w = sys.stdin.readline
n = int(w())
nums = list(map(int, w().split()))
neg_nums = [-i for i in nums]
maxv = 0
for pivot in range(n):
    l = [nums[0]]
    start = 0
    for i in range(1, pivot+1):#LIS
        if nums[i] > l[-1]: # 중복값이 나타났을때 index 조정
            l.append(nums[i])
            start = i
        elif nums[i] < l[-1]:
            idx = bl(l, nums[i])
            l[idx] = nums[i]
    new_s = 1001
    for i in range(start+1,n):
        if nums[i] < l[-1]:
            new_s = i
            break
    if new_s < 1000:
        k = [neg_nums[new_s]]
        for i in range(new_s+1, n):
            if neg_nums[i] > k[-1]:
                k.append(neg_nums[i])
            elif neg_nums[i] < k[-1] and neg_nums[i] > -l[-1]:
                idx = bl(k, neg_nums[i])
                k[idx] = neg_nums[i]
    else:
        k = []
    maxv = max(maxv,len(l)+len(k))
print(maxv)#start가 겹침