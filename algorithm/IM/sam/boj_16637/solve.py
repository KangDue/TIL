import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
괄호추가하기
+-*/ 연산우선순위가 동일할때
괄호를 어디다 씌워야 할까?
중첩괄호x
괄호를 적절히 추가할때 최댓값.
개수 제한 없음.
+-* 뿐이고 모두 0~9 (닫힌구간)의 숫자
괄호안에 연산자는 하나뿐
"""
if __name__ == "__main__":
    import sys
    from collections import deque
    from itertools import combinations
    n = int(input())
    ex = list(input())
    q = deque(ex)

    def cal(x,op,y):
        if op == '*': return int(x)*int(y)
        elif op == '+': return int(x)+int(y)
        else: return int(x)-int(y)

    def result(a): #결과 출력하기
        ans = 0
        while len(q)!=1:
            x=q.popleft()
            op=q.popleft()
            y=q.popleft()
            ans = cal(x,op,y)
            q.appendleft(ans)
        return q[0]

    gwal = [] #괄호 넣은 값 생성. 2*index +1, +2 영역 대체
    for i in range(0,len(ex)-2,2):
        gwal.append(cal(ex[i],ex[i+1],ex[i+2]))
    print(gwal)

    #괄호 넣기
    visited = [0]*len(gwal)
    def sol(a=[],c = 0,idx = 0,op = 0):#괄호넣는 위치 list
        if c == len(gwal):
            print(a)
            return a
        for i in range(c,len(gwal)):
            sol(a+[str(gwal[i])],c+1,op+1,(op+1)*2+1) #괄호 한번 묶으면
            sol(a+ex[2*i:2*i+3],c+1)
    sol()









