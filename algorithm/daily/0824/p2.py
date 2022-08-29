from p1 import Lqueue
v,e = 7,8
info = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
graph = [[] for i in range(v+1)]
for i in range(0,e*2,2):
    graph[info[i]].append(info[i+1])
    graph[info[i+1]].append(info[i])
q = Lqueue()
hist = [1]
q.enqueue(1)
while not q.isEmpty():
    now = q.dequeue()
    hist.append(now)
    for i in graph[now]:
        if i not in hist:
            q.enqueue(i)

    print(now,end=" ")


