import sys
sys.stdin = open('input.txt')
def cal2(x):#후위표현식 계산기
    stack = []
    for i in x:
        try:
            if i.isdigit():
                stack.append(i)
            else:#연산자를 만나면 2개를 뽑아서 계산
                b,a=stack.pop(),stack.pop() #먼저 뽑은게 뒤로감
                stack.append(f'{eval(a+i+b)}') #계산은 eval 활용
        except:#짝이 안맞으면
            print("잘못된 후위표기식입니다.")
            return None
    return stack[0]

#후위표기법으로 출력하기
for t in range(int(input())):
    ex = input()
    # 여는 괄호는 특이하게 넣을때는 최우선으로 막들어가는데 들어가면 순위가 최하위됨.
    # 그래서 일단 넣고 닫는괄호 만나면 만날때까지 pop 실행
    icp = {'+':1,'-':1,'*':2,'/':2,'(':3} # )는 넣으면 바로 pop해야해서 필요 없음
    isp = {'+':1,'-':1,'*':2,'/':2,'(':0}
    op=[]
    ans = ''
    for i in ex:
        if i == ")": #닫는 괄호는 여는괄호 만날때 까지 pop
            while op:
                temp = op.pop()
                if temp == '(':
                    break
                ans += temp
        elif i.isdigit():#그냥 피연산자면 바로 출력
            ans += i
        else: #연산자면 자기랑 같거나 큰 우선순위 연산자는 다 pop한다.(보다 작은걸 만날때 까지)
            while op and isp.get(op[-1]) >= icp.get(i):
                ans += op.pop()
            op.append(i) #연산자 추가
    while op:
        ans += op.pop()
    print(f'#{t+1} {ans}')
    print("계산결과 = ",cal2(ans))





