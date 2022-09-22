import sys
sys.stdin = open('input.txt')
for t in range(1,11):
    T = int(input())
    ladders = [("0"+input()+"0").replace(" ","") for i in range(100)]
    ladders = [ladders[i] for i in range(-1,-101,-1)] #편하게 뒤집기
    y, x = 0, ladders[0].index("p2")
    while y!=99:
        if ladders[y][x + 1] == "1":
            while ladders[y][x + 1] == "1" and x < 100:
                x += 1
            y += 1
        elif ladders[y][x - 1] == "1":
            while ladders[y][x - 1] == "1" and x > 0:
                x -= 1
            y += 1
        else:
            y += 1
    print(f"#{t} {x-1}")#패딩값 빼주기