import sys
sys.stdin = open('input.txt')
"""
괄호 쌍 균형 파악하기 (), []
#stack도 있고 stack에서 규칙을 더 잘 걸어주는법도있고
#문자열을 replace 하는 방법도 있다.
"""
s = '(['
e = '])'
text = input()
while text != '.':
    try:
        stack = []
        for i in text:
            if i in s:
                stack.append(i)
            elif i == ')' and stack.pop()=='(': continue
            elif i == ']' and stack.pop()=='[': continue
            elif i in e:
                print('no')
                text = input()
                break
        else:
            if stack: print('no')
            else: print('yes')
            text = input()
    except:
        print('no')
        text = input()
        continue




