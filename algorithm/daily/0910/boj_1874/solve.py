import sys
sys.stdin = open('input.txt')
#12345678
#43687521
#스택의 넣었다가 뽑아 늘어놓으면서 수열 완성하기
n = int(input())
nums = list(range(n,0,-1))
mine = []
ans = []
for i in range(n):
    x = int(input())
    try:
        if mine:
            if mine[-1] == x:
                mine.pop()
                ans.append('-')
            else:
                while mine[-1] != x:
                    mine.append(nums.pop())
                    ans.append('+')
                ans.append('-')
                mine.pop()
        else:
            mine.append(nums.pop())
            ans.append('+')
            while mine[-1] != x:
                mine.append(nums.pop())
                ans.append('+')
            ans.append('-')
            mine.pop()
    except IndexError:
        print("NO")
        break
else:
    print(*ans,sep='\n')









