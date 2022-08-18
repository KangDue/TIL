import sys
sys.stdin = open('input.txt')

# for t in range(1,int(input())+1):
#     word =[list(input()) for i in range(5)]
#     lmax = len(max(word,key=lambda x:len(x))) #가장 긴 단어 길이
#     word = [i+[""]*(lmax-len(i)) for i in word] #패딩 넣기
#     word = [ ''.join(i) for i in zip(*word)]
#     print(f'#{t}',end=' ')
#     print(*word,sep='')

T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    result = ''

    while True:
        len_list = []
        for j in words:
            len_list.append(len(j))
        min_len = min(len_list) #최소 길이
        max_len = max(len_list) #최대 길이


        if len(words) == 5 : #아직 삭제 안했을때.
            for i in range(min_len): #최소 길이 만큼만 반복해서 가져옴
                for word in words:
                    result += word[i::][0]
        else:# 한놈씩 삭제하고 나서부터
            for k in range(min_len - 1, max_len-1):
                for word in words:
                    result += word[k::][0]

        if max_len != min_len: # 최대 최소가 다르면
            idx = len_list.index(min(len_list)) # 최소길이 삭제
            words.remove(words[idx])

            continue
        else:
            break
    print(result)