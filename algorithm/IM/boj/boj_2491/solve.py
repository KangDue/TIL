import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
LIS 가장 긴 증가 수열
LDS 가장 긴 감소 수열 짬뽕문제
"""
if __name__ == "__main__":
    import sys
    from bisect import bisect_left as bl
    sr = sys.stdin.readline
    n = int(sr())
    nums = [*map(int,sr().split())]
    l = [nums[0]] # 길이 1일대 last부터 k일때 last까지 차곡차곡
    for i in range(1,n):#we must found position in l by bisection method
        if nums[i] >= l[-1]:
            l.append(nums[i])
        elif nums[i] < l[-1]:
            idx = bl(l,nums[i])
            l[idx] = nums[i]
    nnums=[-i for i in nums]
    ll = [nnums[0]]
    for i in range(1,n):#we must found position in l by bisection method
        if nnums[i] > ll[-1]:
            ll.append(nnums[i])
        elif nnums[i] < ll[-1]:
            idx = bl(ll,nnums[i])
            ll[idx] = nnums[i]
    print(max(len(l),len(ll)))
