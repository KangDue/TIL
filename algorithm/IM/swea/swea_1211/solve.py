import sys
sys.stdin = open('input.txt')

d,w,r=int,input,range
for t in r(10):
    w()
    l=[("0"+w()+"0").replace(" ","") for i in r(100)]#0 padding
    mv,idx=10000,0;temp = []
    for n in r(1,101):#모든 경우중 최단거리
        y,x,c=0,n,0 #데이터 타입 확인 잘하자... text int..
        if l[y][x-1] == '0' and l[y][x+1] == '0' and l[y+1][x] == '0': continue # 모두 사다리가 아닌곳은 pass
        else:
            while y<100:#0이 될때 까지
                for i in (-1,1):#좌우
                    if l[y][x+i] == "1":
                        while l[y][x+i] == "1":x+=i;c+=1 #다음값이 유효하면 이동 아니면 stop
                        y+=1;c+=1;break
                else:y+=1;c+=1 #for문 정상종료시
            if mv>c:mv=c;idx=n-1
    print(f"#{t+1} {idx}")#0 padding 고려