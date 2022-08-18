import sys
sys.stdin = open('input.txt',encoding='utf-8')

#괄호검사 #무조건 맞붙어 있는것 부터 지우기
T = int(input())
for t in range(1,T+1):
    text = input()
    bracket = ['[]','{}','()']
    bra_sum = '{}[]()'
    #괄호만 거르기,
    stack = ''.join(filter(lambda x: x in bra_sum,text)) #변수 있는지 잘 확인
    while stack:
        count = 0
        for i in bracket:
            if i in stack:
                count += 1
                pos = stack.find(i)
                stack = stack[:pos] + stack[pos+2:]
        if not(count):#괄호쌍이 없다면
            break
    if not(stack):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')