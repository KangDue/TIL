import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
정말 쉬운문제인데 화가나네...
1. 0도 된다.(음수만 버림)
2. 순서 잘보기 (끝)
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n = int(sr())
    temp=[]
    for i in range(int(0.6*n),n+1): #일일히 모든 수열 처리보니 0.6*n 언저리값
        case = [n,i]
        index = 1
        while case[-1] > -1:
            case.append(case[-2]-case[-1])
        case.pop()
        if len(case) < len(temp):#꼭짓점
            break
        temp = case
    print(len(temp))
    print(*temp)