import sys
sys.stdin = open('input.txt')

d,w,p=int,input,print
for t in range(d(w())):
    info = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    tc, n = w().split();text = w().split()
    p(f'#{t+1}');p(*sorted(text,key=lambda x:info[x]))
    #key='ZRONETWOTHRFORFIVSIXSVNEGTNIN'.find 도 가능