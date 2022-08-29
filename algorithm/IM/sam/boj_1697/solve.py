import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
숨바꼭질
수빈이는 현위치 0~100,000 (닫힌구간)
자기 위치에서 x-1, x+1 또는 2*x로 1초뒤에 이동한다.
시작점 n, 도착점 k
visited check를 할때 유의점...
bit 연산자 ~는 값을 -로 바꿔버리고
^는 xor이라 0과 1이랑 연산시에만 의미있고 외에는 무한루프에 빠질 수 있다.
"""
if __name__ == "__main__":
    import sys
    from collections import deque
    r,sr=range,sys.stdin.readline
    n,k=map(int,sr().split())
    q=deque([[n,0]])
    visited = [0]*100001
    visited[n] = 1
    #필요한가? 의심했지만 필요하다 ㅇㅇ
    #같은위치 돌아오면 결국 선택지는 같다.
    while 1:
        try:
            v,time = q.popleft()
            if v == k:
                print(time)
                raise Exception
            for i in (2*v,v+1,v-1):
                if 0<= i <= 100000: #~는 not 비트 부호 자체를 뒤집어 버린다..
                    if visited[i]^1:
                        q.append([i,time+1])
                        visited[i]=1
        except:break