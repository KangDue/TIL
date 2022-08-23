import sys
sys.stdin = open('input.txt')


def summarize(x):
    x = str(x)
    x_dict = {i: 0 for i in x}
    for i in x:
        x_dict[i] += 1
    return x_dict

T = int(input())
for t in range(1,T+1):
    n = input()
    nd = summarize(n)
    mv = int('9'*len(n))
    n = int(n)
    for i in range(2,10):
        temp = i*n
        if temp > mv:
            break
        elif nd == summarize(temp):
            print(f'#{t} possible')
            break
    else:
        print(f'#{t} impossible')
    if temp>mv:
        print(f'#{t} impossible')