def counting_sort(x):
    if isinstance(x[0],tuple):
        count = [0] * (max(x,key=lambda x:x[0])[0] + 1)  # 0 ~ n 범위
    else:
        count = [0] * (max(x) + 1)  # 0 ~ n 범위
        x = [[i] for i in x] # 감싸주기

    for i in x: #x 요소별 카운팅
        count[i[0]] += 1
    for i in range(1,len(count)): # 누적합 만들어서 랭크 매기기
        count[i] += count[i-1]

    result = [None]*len(x)
    for i in x: # 이 누적합을 통한 배열과정을 안거치면 정렬이 unstable 해짐.
        idx = count[i[0]]
        result[idx-1] = i # 갯수와 index의 차이 고려 -1
        count[i[0]] -= 1
    #원본 x 상에서 먼저 있던 녀석을 뒤쪽부터 앞쪽으로 순서대로 정렬해줌.(중복값도 순서가 존재)
    return result

a = [4,1,5,3,1,6,2,1]
a = [ (a[i],i) for i in range(len(a))] #값, 순서
print(counting_sort(a)) #결과를 보면 딱 안다. 중복값들이 정렬이 되어 있음.