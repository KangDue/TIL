o = open('input.txt')
n = int(next(o))
o = [*map(lambda x:[*map(int,x.split())],o)]
def msort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    lower = msort(arr[:mid])
    upper = msort(arr[mid:])

    merged = []
    u=l=0
    while l < len(lower) and u < len(upper):
        if lower[l][1] < upper[u][1]:
            merged.append(lower[l])
            l += 1
        elif lower[l][1] == upper[u][1]:
            if lower[l][0] < upper[u][0]:
                merged.append(lower[l])
                l += 1
            else:
                merged.append(upper[u])
                u += 1
        else:
            merged.append(upper[u])
            u += 1
    merged += lower[l:] + upper[u:]
    return merged

for i in msort(o):
    print(*i)
