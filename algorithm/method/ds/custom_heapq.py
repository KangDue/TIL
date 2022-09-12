o = open('input.txt')
# 아래는 수제작 버전.
nones = [] #nones index list를 만들어서 써보자
def add(q,x):
    if x:
        if nones: #실제 heap같은 속도의 처리는 안됨..
            idx = nones.pop()
            q[idx] = x
        else:
            q.append(x)
            idx = len(q)-1
        while idx:
            parent = (idx-1)//2
            if q[idx] < q[parent]: #부모노드보다 작으면 값 교체
                q[idx],q[parent] = q[parent],q[idx]
            else: #아니면 종료
                break
            idx = parent
    else: pop(q)

def pop(q):
    if q==[] or q[0] == None:
        print(0);return 0
    print(q[0])
    idx = 0
    while 1:
        t1=t2=None
        if idx*2+1 < len(q):
            t1 = q[idx*2+1]
        if idx*2+2 < len(q):
            t2 = q[idx*2+2]
        if t1 or t2:
            if t1 and t2: q[idx],idx = min( (q[idx*2+1],idx*2+1),(q[idx*2+2],idx*2+2) )
            elif t1: q[idx],idx = q[idx*2+1],idx*2+1
            elif t2: q[idx],idx = q[idx*2+2],idx*2+2
            else: break
        else: break
    q[idx] = None
    nones.append(idx)
q = []
n = int(next(o))
for x in o:
    add(q,int(x))