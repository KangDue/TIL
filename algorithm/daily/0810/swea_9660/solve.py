import itertools as it

temp = list(it.permutations([1,2,3,4],4))
print(len(temp))

temp2 = []
for i in temp:
    if i[0] != 1 and i[1] != 1 and i[2] != 3 and i[3] != 4:
        temp2.append(i)
print(len(temp2))

ans = list(range(4,0,-1))
print(ans)