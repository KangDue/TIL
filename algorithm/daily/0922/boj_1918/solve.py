import sys
sys.stdin = open('input.txt')
"""
후위 표기식

"""
ex = input()
out = {'(':3,'+':1, '-':1, '*':2,'/':2,')':0} #우선순위 대략 이런느낌
# (가 뽑을때 우선순위가 3이 아니면 (가 들어갈때마다 뒤에 다뽑아버리거나 (만 따로 처리 해줘야함.
# 여러가지로 처리 가능
stack = []
ans = ''
#자기보다 우선순위 작은놈 만날때까지 다뺌.
for i in ex:
    if i.isalpha():
        ans+=i
    else:
        while stack:
            if out[stack[-1]] >= out[i]:
                if i==')' and stack[-1] == '(': #여는괄호 만나면 닫는괄호까지 달려가기
                    stack.pop();break
                else:
                    if stack[-1]=='(': #여는괄호가 아니면 닫는괄호 전에서 멈춰줘야함.
                        break
                    ans += stack.pop()
            else:
                break
        if i != ')':
            stack.append(i)
while stack:
    ans+=stack.pop()
print(ans)

# ABC*+DE/-