import sys
sys.stdin = open('input.txt',encoding='utf-8')
class Link:
    def __init__(self,value=None,child=None):
        self.value = int(value)
        self.child = child
for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    arrays = [ list(map(Link,input().split())) for i in range(m)]
    for i in range(n):
        for k in range(m-1): #링크로 연결하기
            arrays[i][k].child = arrays[i][k+1]
    Head = arrays[0][0]
    p = Head
    i = 1
    while i < n:
        if p.child == None:
            p.child = arrays[i][0]
            p = Head
            i += 1
            continue
        if Head.value > arrays[i][0].value:
            x = Head
            Head = arrays[i][0]
            arrays[i][-1].child = x
            p = Head
            i += 1
            continue
        if p.child.value > arrays[i][0].value: #자식의 값 비교
            p.child, arrays[i][-1].child = arrays[i][0], p.child
            p = Head
            i += 1
            continue
        # 크지 않으면 다음 노드로
        p = p.child
    p = Head
    ans = []
    while p:
        ans.append(p.value)
        p = p.child
    ans.reverse()
    print(f'#{t}',end=' ')
    print(*ans[:10])

    """
    아래와 같이하면 linked list 보다 느리다.
    """
    # for i in range(1,n): #0번째 어레이 기준으로 나머지를 계속 삽입 #통째로 삽입하고 확인하긴 불편하니 리스트 별로 확인
    #     for k in range(0,i):
    #         for j in range(m):
    #             if arrays[k][j].value > arrays[i][0].value: #insert 할 녀석의 첫 값보다 큰 값 찾으면
    #                 arrays[k][j-1].child = arrays[i][0]
    #                 arrays[i][-1].child = arrays[k][j]
    #                 break
    #     else:# 큰 값이 없으면 마지막에 추가
    #         arrays[k][-1].child = arrays[i][0]
    # t = arrays[0][0]
    # for i in range(n*m):
    #     print(t.value)
    #     t = t.child

    # for i in range(1,m):
    #     for k in range(m):
    #         if arrays[0][k] > arrays[i][0]:
    #             arrays[0] = arrays[0][:k] + arrays[i] + arrays[0][k:]
    #             break
    #     else:
    #         arrays[0] = arrays[0] + arrays[i]
    # arrays[0].reverse()
    # print(f'#{t}',end=" ")
    # print(*arrays[0][:10])
    # 최종 배열을 뒤집고하는건 속도에 큰 영향 없음.
