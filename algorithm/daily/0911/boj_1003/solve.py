import sys
sys.stdin = open('input.txt')
"""
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐p2);
    }
}
위 함수에서 0과 1이 출력되는 횟수를 구하시오.
"""
for t in range(int(input())):
    n = int(input())
    if n == 0: print(1,0)
    elif n == 1: print(0,1)
    else:
        z0,z1 = 1,0
        o0,o1 = 0,1
        for i in range(2,n+1):
            zero = z0 + z1
            z0, z1 = z1, zero
            one = o0 + o1
            o0,o1 = o1,one
        print(zero,one)
#잘보면 각각의 피보나치임

