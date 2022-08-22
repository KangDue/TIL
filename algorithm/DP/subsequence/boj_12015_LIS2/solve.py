import sys
sys.stdin = open('input.txt')


if __name__ == "__main__":
    import sys
    from bisect import bisect_left as bl
    w = sys.stdin.readline
    n = int(w())
    nums = list(map(int,w().split()))
    l = [nums[0]] # 길이 1일대 last부터 k일때 last까지 차곡차곡
    for i in range(1,n):#we must found position in l by bisection method
        if nums[i] > l[-1]:
            l.append(nums[i])
        elif nums[i] < l[-1]:
            idx = bl(l,nums[i])
            l[idx] = nums[i]
    print(len(l))