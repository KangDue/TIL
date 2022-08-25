import sys
sys.stdin = open('input.txt')

d,w,r=int,input,range
for t in r(10):
    v,e=map(d,w().split())
    o=[*map(d,w().split())]
    g={i:[] for i in r(1,v+1)}#각 노드의 부모 정보 담는 딕셔너리
    task=[] #순서대로 작업 담아올 list
    for i in r(0,e*2,2):
        g[o[i+1]].append(o[i])#정보 입력
    while g:
        temp=g.copy()#pop해줘서 길이가 변하므로 복사본 생성
        for i in temp:
            if g[i] == []:#부모 노드가 없으면 작업해도됨.
                for j in g.keys():#다른 작업들중 자신이 부모노드인거 전부 제거
                    if i in g[j]:g[j].remove(i)
                task+=[i];g.pop(i)#task에 추가하고 자기를 g에서 삭제
    print(f"#{t+1}",*task)

#제출용 short
"""
d,w,r=int,input,range
for t in r(10):
    v,e=map(d,w().split());o=[*map(d,w().split())];g={i:[] for i in r(1,v+1)};s=[]
    for i in r(0,e*2,2):g[o[i+1]].append(o[i])
    while g:
        c=g.copy()
        for i in c:
            if g[i] == []:
                for j in g.keys():
                    if i in g[j]:g[j].remove(i)
                s+=[i];g.pop(i)
    print(f"#{t+1}",*s)
"""