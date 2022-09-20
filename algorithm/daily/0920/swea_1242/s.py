import sys
sys.stdin = open('input.txt')
d = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
hb = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
def mag(x,size=1):#비율 축소하는 녀석.
    res=[]
    for i in range(0,len(x),size):
        res.append(x[i])
    return ''.join(res)
def lts(arr):
    ans=''
    for i in arr:
        ans+=str(i)
    return ans
R,I=range,input
for t in R(int(I())):#
    n,m=map(int,I().split())
    valid,valid_code,ans=set(),set(),0
    for _ in R(n):
        p=I()
        if p!='0'*m:
            for i in p.split('0'*14):
                valid.add(i)
    for i in valid:
        temp='0'*16
        for hc in i:
            temp+=hb.get(hc,'')
        size,pivot=1,len(temp)
        while size < m//4:
            a=80;idx=temp[:pivot].rfind('1')+1
            while idx-56*size>0 and temp[idx-1]=='1':
                try:
                    s=[]
                    for j in range(idx-56*size,idx,7*size):
                        s.append(d[mag(temp[j:j+7*size],size)])
                    vc=s.pop()
                    if not (sum(map(lambda x: s[x] * (1 + 2 * (x % 2 == 0)), R(7))) + vc) % 10:
                        sl=(lts(s+[vc]))
                        if not valid_code.issuperset({sl}):valid_code.add(sl);a=min(a,sum(s)+vc)
                    pivot = idx-56*size
                    break
                except:idx-=size
            else:size+=1;continue
            if a<80:ans+=a
            size=1
    print(f'#{t+1} {ans}')
#메모리 에러 뜨는거 같은데...? 가 아니라 input에서 이상한 값이 나와서 dict에서 hashing 할때 오류 발생.
#0을 다잘라버려서 앞의 0이 필요할 수 도 있음 그래서 temp = '0'*16