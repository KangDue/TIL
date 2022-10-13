"""
Brainf**k 이 프로그램이 끝나는지. 무한루프에 빠지는지?
하나의 정수 배열, 그 포인터,
- " 포인터 수 1 감소 ( 2**8 로 나눈 나머지)
+ 포이터 수 1 증가 ( 2**8 로 나눈 나머지)
< 왼쪽으로 포인터 한칸
> 오른쪽으로
[ 가리키는 수가 0이면 ]의 다음 명령으로 점프
] 0이 아니라면 [의 다음 명령으로 점프
. 가리키는 수 출력
, 문자 하나를 읽고 포인터가 가리키는 곳에 저장, 입력의 마지막은(EOF)는 255 저장

배열은 처음 0을 가리키고, - indexing, index초과시 처음으로 돌아옴.
[] 항상 pair가 존재 , loop를 뜻함.
"""
import sys,time
sys.stdin = open('input.txt')
st = time.time()
pair = {'[':']', ']':'['}
# def find_pair(idx,f):
#     stack = [f]
#     if f == '[':
#         while stack:
#             idx += 1
#             if code[idx] == f:
#                 stack.append(f)
#             elif code[idx] == pair[f]:
#                 stack.pop()
#     elif f == ']':
#         while stack:
#             idx -= 1
#             if code[idx] == f:
#                 stack.append(f)
#             elif code[idx] == pair[f]:
#                 stack.pop()
#     return idx

def find_pair(sp):
    for i in range(cs):
        if code[i] == '[':
            sp += 1
            stack[sp] = i
        if code[i] ==']':
            pair_dict[i] = stack[sp]


for t in range(int(input())):
    ms,cs,isize = map(int,input().split()) #메모리, 코드크기, 입력크기
    arr = [0]*ms
    code = input()
    text = input() #읽을 문자열
    p = 0 #포인터
    pair_dict = {}
    # for i in range(cs):
    #     if code[i]=='[':
    #         temp = find_pair(i,'[')
    #         pair_dict[i] = temp
    #         pair_dict[temp] = i
    cnt = 0
    idx = ddx = 0  # 코드위치
    mcode = 0  # 최대 코드 인덱스
    stack = [0]*5000
    stack_pos = [0]*5000
    sp = 0
    while idx < cs:
        cnt += 1
        if code[idx] == '-':
            arr[p] -= 1
            if arr[p] == -1:
                arr[p] = 255
        elif code[idx] == '+':
            arr[p] += 1
            if arr[p] == 256:
                arr[p] = 0
        elif code[idx] == '<':
            p -= 1
            if p == -1:
                p = ms -1
        elif code[idx] == '>':
            p += 1
            if p == ms:
                p = 0
        elif code[idx] == '[':
            if not arr[p]:
                idx = pair_dict[idx]
        elif code[idx] == ']':
            if arr[p]:
                idx = pair_dict[idx]
                stack_pos[sp-1] = cnt
        elif code[idx] == '.': #가리키는 수 출력
            pass
        elif code[idx] == ',': #읽고 포인터 위치에 저장
            if ddx < isize:
                arr[p] = ord(text[ddx])
                ddx += 1
            else:
                arr[p] = 255
        idx += 1
        mcode = max(mcode, idx)
        if cnt >= 50000000:
            print(f'Loops {pair_dict[mcode]} {mcode}')
            break
    else:
        print("Terminates")
#53분 경과 일시 정지
et = time.time()
print(et-st,'sec')
