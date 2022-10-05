c=0
def sep(start,end,h=0):
    global minv, pivot,a,b
    if h > pivot:
        return -1
    if start<= a <= end and start<= b <= end:
        minv = min(minv,pivot-h)
    sep(start,end//2,h+1)
    sep(end//2+1,end,h+1)

for a in range(1,11):
    for b in range(1,11):
        N = 1<<(max(a,b)).bit_length()
        pivot = (N - 1).bit_length()
        minv = (N - 1).bit_length()
        sep(1, N, h=0)
        t1 = minv
        t2 = ((a-1)^(b-1)).bit_length()
        print(minv,t2)
        if t1!=t2:
            c +=1
print(c)