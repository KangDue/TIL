import sys
sys.stdin = open('input.txt')
ans = 1
for i in range(2,int(input())+1):
    ans *= i
print(ans)
