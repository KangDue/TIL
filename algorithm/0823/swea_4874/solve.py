import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    ex = input().split()
    stack = []
    for i in ex:
        try:
            if i.isdigit():
                stack.append(i)
            elif i == '.':
                break
            else:
                b, a = int(stack.pop()), int(stack.pop())
                if i == '*': stack.append(a * b)
                elif i == '/': stack.append(a // b)
                elif i == '+': stack.append(a + b)
                else: stack.append(a - b)
        except:
            break
    if len(stack) == 1: #정상적인 연산뒤엔 1개만 남음
        print(f'#{t + 1} {stack[-1]}')
    else:
        print(f'#{t + 1} error')