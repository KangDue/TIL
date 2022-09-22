import sys
import math
math.prod()
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    n = int(input())
    if n <
    point = [tuple(map(int,input().split())) for i in range(n)]
    vec = []
# a = (1,3,p2)
# b = (3,-1,6)
# c = (5,p2,0)
# point = [a,b,c]
# vec = []
    if n > 3:
        for i in range(2):
            vec.append([point[i+1][0]-point[0][0],
                        point[i+1][1]-point[0][1],point[i+1][2]-point[0][2]])
    # A(x-a0) + B(y-a1) + C(z-a2) = 0
    # Ax + By + Cz = R 이 평면의 방정식
        A = vec[0][1]*vec[1][2]-vec[0][2]*vec[1][1]
        B = -( vec[0][0]*vec[1][2] - vec[0][2]*vec[1][0] )
        C = vec[0][0]*vec[1][1] - vec[0][1]*vec[1][0]
        R = A*point[0][0] + B*point[0][1] + C*point[0][2]

        def cal(A,B,C,x):
            return A*x[0] + B*x[1] + C*x[2]

        def cross(a,b):
            A = a[1]*b[2]-a[2]*b[1]
            B = -(a[0]*b[2] - a[2]*b[1])
            C = a[0]*b[1]-a[1]*b[0]
            if A*B*C == 0: #한 직선위의 점이면
                return 0
            else:
                A, B, C

        if cross(a,b): # 한 직선위의 점이 아니면
            for i in point:
                if cal(A, B, C, i) != R:
                    print(f"#{t} NIE")
                    break
            else:
                print(f"#{t} TAK")
        else:



        for i in point:
            if cal(A,B,C,i) != R:
                print(f"#{t} NIE")
                break
        else:
            print(f"#{t} TAK")
    else:
        print(f"#{t} TAK")
## swea test case 9, 12번은 TAK아니고 NIE임, 왜이러지 ?