import sys
sys.stdin = open('input.txt')

#압축버젼
w,d=input,int

def cal2(x):#후위표현식 계산기
    stack = []
    for i in x:
        if i.isdigit():
            stack.append(i)
        else:#연산자를 만나면 2개를 뽑아서 계산
            b,a=stack.pop(),stack.pop() #먼저 뽑은게 뒤로감
            r = d(a) * d(b) if i == '*' else d(a) + d(b)
            stack.append(f'{r}')
    return stack[0]

for t in range(10):
    n,ex=w(),w()
    icp = {'+':1,'*':2,'(':3} # )는 넣으면 바로 pop해야해서 필요 없음
    isp = {'+':1,'*':2,'(':0}
    op=[]
    a=''
    for i in ex:
        if i == ")": #닫는 괄호는 여는괄호 만날때 까지 pop
            while op:
                temp = op.pop()
                if temp == '(':
                    break
                a += temp
        elif i.isdigit():#그냥 피연산자면 바로 출력
            a += i
        else: #연산자면 자기랑 같거나 큰 우선순위 연산자는 다 pop한다.(보다 작은걸 만날때 까지)
            while op and isp.get(op[-1]) >= icp.get(i):
                a += op.pop()
            op.append(i) #연산자 추가
    while op:
        a += op.pop()
    print(f'#{t+1} {cal2(a)}')


