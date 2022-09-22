import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
#나머지 연산...
#핵심= 반사된다고 하지만 상하/ 좌우 는 결국 순환할 뿐이다. 1234321 같이 순환됨. 나머지 연산 활용
#진짜 반사되게 푸는 방식도 있는데 그게 왜 틀린지 edge case를 못찾겠다.
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    w,h = map(int,sr().split())
    x,y = map(int,sr().split())
    hour = int(sr())

    print((x+hour)%w,(y+hour%h))

r,d=input,int;w,h=map(d,r().split());x,y=map(d,r().split());s=d(r());print((x+s)%w,(y+s)%h)

# r,d,z=input,int,range;w,h=map(d,r().split());x,y=map(d,r().split());xr=[i for i in z(w)]+[i for i in z(w,0,-1)];yr=[i for i in z(h)]+[i for i in z(h,0,-1)];s=d(r());print(xr[(x+s)%(w*p2)],yr[(y+s)%(h*p2)])
