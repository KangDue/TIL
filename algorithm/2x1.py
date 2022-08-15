import queue
def X(tup):
    return (tup[0]+1,2*tup[1],tup[2]+"X")
def Y(tup):
   return (tup[0]*2,tup[1]+1,tup[2]+"Y")
kv = {}
alls = {}
for i in range(1):
    for k in range(i,100):
        a,b=i,k
        q = queue.Queue()
        q.put((a,b,""))
        temp = kv.get((a,b))
        ans = ""
        if temp:
            while temp:
                ans += temp[2]
                temp = kv.get(temp[:2])
            print(f'#{0} {ans}')
            alls.setdefault((a, b), ans)
        else:
            while 1:
                now = q.get()
                if now[0] == now[1]:
                    break
                else:
                    q.put(X(now))
                    q.put(Y(now))
                arr_temp = []
                for z in now[2]:
                    if z == "X":
                        kv.setdefault((a,b),(a+1,2*b,"X"))
                        a ,b = a+1, 2*b
                    else:
                        kv.setdefault((a,b),(2*a,b+1,"Y"))
                        a, b = 2*a, b+1
            alls.setdefault((a, b), now[2])
            print(f'#{1} {now[2]}')