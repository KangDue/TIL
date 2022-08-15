import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    num = list(map(int,input()))
    cnum = num[:]
    for i in range(len(num)-1):
        if num[i] < max(num[i+1:]):
            idx1 = num[-1:-len(num)-1:-1].index(max(num[i + 1:])) #중복이면 가장 뒤에걸 가져와야함.
            idx2 = -(idx1+1)
            temp = num[idx2]
            num[idx2] = num[i]
            num[i] = temp
            break
    maxv = num[:]

    change = 0
    temp = set(cnum[1:])
    temp.discard(0)
    temp = tuple(temp)
    if temp and cnum[0] > min(temp): #첫칸을 바꿧다면?
        idx1 = cnum[-1:-len(cnum) - 1:-1].index(min(temp))  # 중복이면 가장 뒤에걸 가져와야함.
        idx2 = -(idx1 + 1)
        temp = cnum[idx2]
        cnum[idx2] = cnum[0]
        cnum[0] = temp
        change = 1
    if change == 0:
        for i in range(1,len(cnum) - 1):
            if cnum[i] > min(cnum[i + 1:]):
                idx1 = cnum[-1:-len(cnum) - 1:-1].index(min(cnum[i + 1:]))  # 중복이면 가장 뒤에걸 가져와야함.
                idx2 = -(idx1 + 1)
                temp = cnum[idx2]
                cnum[idx2] = cnum[i]
                cnum[i] = temp
                break
    minv = cnum[:]
    minv = ''.join([str(i) for i in minv])
    maxv = ''.join([str(i) for i in maxv])
    print(f"#{t} {minv} {maxv}")