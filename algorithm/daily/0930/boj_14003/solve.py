import sys
sys.stdin = open('input.txt')
"""
LCS - 5 , 이하 문제들은 다 같거나 더 범위가 작고 쉬운 문제이므로 pass
pointer를 활용해 이전 값을 추적한다.
값이 중간에 교체 되더라도 괜찮다.
"""
class point:
    def __init__(self,value,parent=None):
        self.parent = parent
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value
    def __le__(self, other):
        return self.value <= other.value


if __name__ == "__main__":
    import sys
    from bisect import bisect_left as bl
    from collections import deque
    w = sys.stdin.readline
    n = int(w())
    nums = list(map(lambda x:point(int(x)),w().split()))
    each = [nums[0]]# 길이 1일때 last부터 k일때 last까지 차곡차곡
    for i in range(1,n):#we must found position in l by bisection method
            if nums[i] > each[-1]:
                nums[i].parent = each[-1]
                each.append(nums[i])

            elif nums[i] <= each[-1]:
                idx = bl(each, nums[i])
                if idx:
                    nums[i].parent = each[idx-1]
                each[idx] = nums[i]
    p = each[-1]
    ans = []
    while p:
        ans.append(p)
        p = p.parent
    ans.reverse()
    print(len(ans))
    print(*ans)