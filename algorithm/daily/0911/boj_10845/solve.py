o = open('input.txt')
o = [*map(str.split,list(o))]
front = -1
rear = -1
q = []
for i in range( 1, int(o[0][0]) + 1 ):
    order = o[i][0]
    if order == 'push':
        q.append(o[i][1])
        rear += 1
    elif order == 'pop':#앞에서 팝
        if front == rear:
            print(-1)
        else:
            front += 1
            print(q[front])
    elif order == 'size':
        print(rear-front)
    elif order == 'front':
        if front == rear:
            print(-1)
        else:
            print(q[front+1])
    elif order == 'back':
        if front == rear:
            print(-1)
        else:
            print(q[rear])
    elif order == 'empty':
        print(+(rear == front))
