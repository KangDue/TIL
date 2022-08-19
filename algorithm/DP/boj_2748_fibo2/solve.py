import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    import sys
    fibo = [0,1]*90 # 0 padding + 1~90
    for i in range(2,91):
        fibo[i] = fibo[i-1] + fibo[i-2]

    n = int(sys.stdin.readline())
    print(fibo[n])





