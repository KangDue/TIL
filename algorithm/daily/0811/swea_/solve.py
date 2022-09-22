import sys
sys.stdin = open('input.txt')
for t in range(1,11):
    T = int(input())
    ladders = [input().replace(" ","") for i in range(100)]
    ladders = [ladders[i] for i in range(-1,-101,-1)] #편하게 뒤집기
    a,b = ladders[0].index("p2"), 0
    while b != 99:
        try:
            temp1 = ladders[b][a+1] == "1" and a < 99
        except:#벽에 붙어버리면 index에러뜨니까 False처리
            temp1 = False
        try:
            temp2 = ladders[b][a-1] == "1" and a > 1
        except:#벽에 붙어버리면 index에러뜨니까 False처리
            temp2 = True
        temp3 = ladders[b+1][a] == "1"

        if temp1: #앞옆 갈림길은 무조건 옆으로 이동
            try:
                while ladders[b][a+1] == "1" and a < 99:
                    a += 1
            except:
                False
            b+=1
        elif temp2: #앞옆 갈림길은 무조건 옆으로 이동
            try:
                while ladders[b][a-1] == "1" and a > 1:
                    a -= 1
            except:
                pass
            b+=1
        else: #양 옆 갈곳 없으면 아래로
            b += 1
    print(f"#{t} {a}')