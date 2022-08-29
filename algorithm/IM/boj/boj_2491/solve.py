import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
LIS 가장 긴 증가 수열
LDS 가장 긴 감소 수열 짬뽕문제
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n = int(sr())
    nums = [*map(int,sr().split())]
    maxv = 1
    t1=t2=1 #원소하나가 최소
    for i in range(1,n):
        if nums[i-1] >= nums[i]:#감소수열
           t1 += 1
        else: maxv = max(maxv,t1); t1 = 1
        if nums[i-1] <= nums[i]:#증가수열
            t2 += 1
        else: maxv = max(maxv,t2); t2 = 1
    #마지막 값.. 챙겨줘야함
    maxv = max(t1,t2,maxv) #마지막에 else를 못거치고 나오면 비교 한 번 더
    print(maxv)

