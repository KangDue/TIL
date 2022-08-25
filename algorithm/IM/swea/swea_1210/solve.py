import sys
sys.stdin = open('input.txt')

d,w,r=int,input,range
for t in r(10):
    w()#tc 번호
    l=[("0"+w()+"0").replace(" ","") for i in r(100)]#0 padding
    y,x=99,l[-1].index("2")
    while y:#0이 될때 까지
        for i in (-1,1):#좌우
            if l[y][x+i] == "1":
                while l[y][x+i] == "1":x+=i; #다음값이 유효하면 이동 아니면 stop
                y-=1;break
        else:y-=1; #for문 정상종료시
    print(f"#{t+1} {x-1}")#0 padding 고려
