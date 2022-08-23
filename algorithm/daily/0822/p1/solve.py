import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    ex = input()
    ops = '*/+-'
    op=[]
    ans = f'#{t+1} '
    for i in ex:
        if i in ops:
            op.append(i)
        else:
            ans += i
    while op:
        ans += op.pop()
    print(ans)