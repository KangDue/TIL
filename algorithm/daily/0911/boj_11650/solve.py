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
    l=u=0
    while l < len(lower) and u < len(upper):
        if lower[l][0] < upper[u][0]:
            merged.append(lower[l])
            l += 1
        elif lower[l][0] == upper[u][0]:
            if lower[l][1] < upper[u][1]:
                merged.append(lower[l])
                l+=1
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

#삽입정렬 시간초과뜸 ㅎㅎ;
# for i in range(1,n):
#     for j in range(i,0,-1):
#         if o[j][0] < o[j-1][0]:
#             o[j], o[j-1] = o[j-1], o[j]
#         elif o[j][0] == o[j-1][0]:
#             if o[j][1] < o[j-1][1]:
#                 o[j], o[j - 1] = o[j - 1], o[j]
#         else:
#             break

#여기선 신기하게 pypy가 python3보다 2배 빠름
#물론 메모리차지는 그 반대