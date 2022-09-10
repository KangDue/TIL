import sys
sys.stdin = open('input.txt')
for t in range(int(input())):
    PS = list(input())
    PS.reverse()
    stack = []
    while PS:
        temp = PS.pop()
        if temp == '(':
            stack.append(temp)
        else: #닫는괄호
            if stack and stack.pop() == '(': continue
            else:
                print('NO')
                break
    else:
        if stack: print('NO')
        else: print('YES')
