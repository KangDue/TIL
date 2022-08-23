cnt = 0
subs = []
def check(sums,n,start):
    global cnt
    if sum(sums) > n:
        return None
    if sum(sums) == n:
        cnt += 1
        subs.append(sums)
        return None
    for i in range(start,n+1): #진부분집합
        check(sums+[i],n,i+1)
check([],10,1)
print(subs,"의 총 개수는",cnt)