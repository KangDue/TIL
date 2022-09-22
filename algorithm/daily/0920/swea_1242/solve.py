import sys
sys.stdin = open('input.txt')
"""
단순 2진 암호코드
코드는 8자리이며, 
올바른건 홀수 자리 합 *3, 짝수자리합 = 10의 배수
스캐너는 암호코드 1개가 포함된 직사각형 배열을 읽는다.
암호코드 이외의 부분은 전부 0
코드에서 숫자 1개는 7개으 비트로 암호화되어 주어짐.
8자리중 앞 7자리는 수 계산 마지막은 검증 코드
16진수 배열을 2진수로 변환하고 그 안에 포함되어 있는 암호코드 정보를 확인.
암호 코드하나는 숫자 8개, 붙어있지는 않음. 5~100칸 사이 길이

"""
d = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

#숏버전
d = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
# R,I=range,input
# for t in R(int(I())):
#     n,m=map(int,I().split());a=80
#     for _ in R(n):
#         p=I()
#         for i in d:
#             x=p.find(i)
#             if -1<x<m-56:
#                 s = []
#                 for i in R(x,x+56,7):
#                     s.append(d.get(p[i:i+7],100))
#                 if not sum(map(lambda x:s[x]*(1+p2*(x%p2==0)),R(8)))%10:a=min(a,sum(s))
#     print(f'#{t+1} {(a<80)*a}')


d = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
def h2b(x):
    ans = ''
    for i in x:
        ans += f'{int(i,16):04b}'
    return ans

def mag(x,size=1):#비율 축소하는 녀석.
    res = []
    for i in range(0,len(x),size):
        res.append(x[i])
    return ''.join(res)

def l_to_s(arr):
    ans = ''
    for i in arr:
        ans+=str(i)
    return ans

#14, 28, 56, 112
# 16진수코드 길이 // 14  = 비례 size

R,I=range,input
for t in R(int(I())):
    n,m=map(int,I().split())
    valid = dict() #15자리 16진수 모여야함.,14자리면 그냥 끝 7*8 되서 쉬워짐
    for _ in R(n):
        p=I()
        print(p.split('00000000000000'))
        if p != '0'*m:
            valid[p] = 1
    #16진수 코드만 걸러냄. 이를 다시 2진수 코드로 변환.
    #코드는 항상 1로 끝남. 1로끝난 지점부터 -56 지점에서 시작하면 됨.
    ans = [] #유효 코드 계산값 받아오기
    valid_code = dict()

    for i in valid:
        temp = h2b(i)
        size = 1 # 초기 size
        while size < m//4:
            a = 80
            idx = temp.rfind('1') + 1
            while idx-56*size>0 and temp[idx-1] == '1': #마지막 자리가 1이라도 유효하지 않을수 있으니 뒤에서부터 반복
                try:
                    new = temp[idx-56*size:idx]
                    s = []
                    for j in range(0,56*size,7*size):
                        s.append(d[mag(new[j:j+7*size],size)])
                    vc = s.pop()
                    if not (sum(map(lambda x: s[x] * (1 + 2 * (x % 2 == 0)), R(7))) + vc) % 10:
                        strlist = l_to_s(s+[vc])
                        if valid_code.get(strlist):
                            pass
                        else:
                            valid_code[strlist]=1
                            a = min(a, sum(s) + vc)
                    temp = temp[:idx-56*size]
                    break #정상 동작시 종료
                except:
                    idx -= size
                #print(temp,idx)
            else:
                size += 1; continue #정상적으로 내부 와일문 실행이 종료되면 , SIZE 늘려서 다시 확인

            if a < 80:
                ans.append(a)
            size = 1
    print(f'#{t+1} {sum(ans)}')


# def h2b(x):
#     ans = ''
#     for i in x:
#         ans += f'{int(i,16):04b}'
#     return ans
#
# def mag(x,size=1):#비율 축소하는 녀석.
#     res = []
#     for i in range(0,len(x),size):
#         res.append(x[i])
#     return ''.join(res)
#
# def l_to_s(arr):
#     ans = ''
#     for i in arr:
#         ans+=str(i)
#     return ans
#
# #14, 28, 56, 112
# # 16진수코드 길이 // 14  = 비례 size
#
# R,I=range,input
# for t in R(int(I())):
#     n,m=map(int,I().split())
#     valid = dict() #15자리 16진수 모여야함.,14자리면 그냥 끝 7*8 되서 쉬워짐
#     for _ in R(n):
#         p=I()
#         if p != '0'*m:
#             valid[p] = 1
#     #16진수 코드만 걸러냄. 이를 다시 2진수 코드로 변환.
#     #코드는 항상 1로 끝남. 1로끝난 지점부터 -56 지점에서 시작하면 됨.
#     ans = [] #유효 코드 계산값 받아오기
#     valid_code = dict()
#     for i in valid:
#         temp = h2b(i)
#         size = 1 # 초기 size
#         while 1:
#             a = 80
#             idx = temp.rfind('1') + 1
#             if idx == 0 or size >= m//4:
#                 break
#             while temp[idx-1] == '1': #마지막 자리가 1이라도 유효하지 않을수 있으니 뒤에서부터 반복
#                 try:
#                     new = temp[idx-56*size:idx]
#                     s = []
#                     for j in range(0,56*size,7*size):
#                         s.append(d[mag(new[j:j+7*size],size)])
#                     vc = s.pop()
#                     if not (sum(map(lambda x: s[x] * (1 + p2 * (x % p2 == 0)), R(7))) + vc) % 10:
#                         strlist = l_to_s(s+[vc])
#                         if valid_code.get(strlist):
#                             pass
#                         else:
#                             valid_code[strlist]=1
#                             a = min(a, sum(s) + vc)
#                     temp = temp[:idx-56*size] # 축소
#                     break #정상 동작시 종료
#                 except:
#                     idx -= size
#                 #print(temp,idx)
#             else:
#                 size += 1; continue #정상적으로 내부 와일문 실행이 종료되면 , SIZE 늘려서 다시 확인
#
#             if a < 80: ans.append(a); a = 80;size = 1 ;continue
#
#     print(sum(ans))