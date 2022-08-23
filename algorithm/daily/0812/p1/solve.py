def my_len(arr):
    # \0 만나기 전까진 개수 세고 만나면 종료
    return arr[:arr.index('\0')],arr.index('\0')

#문자열상 사전 순서 a가 앞이면 1, b가 앞이면 -1
def str_compare(a,b):
    if len(a) > len(b):
        for i in range(len(b)):
            if ord(a[i])<ord(b[i]):
                print(f'{a}가 먼저입니다.')
                return ord(a[i])-ord(b[i])
            elif ord(a[i])>ord(b[i]):
                print(f'{b}가 먼저입니다.')
                return ord(a[i])-ord(b[i])
        else:
            print(f'{a}가 먼저입니다.')
            return 1 #b가 a에 포함
    elif len(a) < len(b):
        for i in range(len(a)):
            if ord(a[i])<ord(b[i]):
                print(f'{a}가 먼저입니다.')
                return ord(a[i])-ord(b[i])
            elif ord(a[i])>ord(b[i]):
                print(f'{b}가 먼저입니다.')
                return ord(a[i])-ord(b[i])
        else:
            print(f'{b}가 먼저입니다.')
            return -1 #a가 b에 포함
    else: # 같으면
        for i in range(len(a)):
            if ord(a[i])<ord(b[i]):
                print(f'{a}가 먼저입니다.')
                return ord(a[i])-ord(b[i])
            elif ord(a[i])>ord(b[i]):
                print(f'{b}가 먼저입니다.')
                return ord(a[i])-ord(b[i])
        else:
            print(f'{a} 와 {b}는 같습니다.')
            return 0 #둘이 완전 일치
# repr은 객체 자체를 문자로 변환
#str = 객체를 문자열 형태의 자료형으로 변환