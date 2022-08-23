import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    so = input().replace(" ","")
    prob = 15 - len(so)
    #남는 판수가 있을때
    win = so.count("o")
    if win + prob >= 8:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO") # 도저히 왜틀렸는지 모르겠어서 봤는데 No라고 했었다 ...