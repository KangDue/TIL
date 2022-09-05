import sys
sys.stdin = open('input.txt')
import sys
for i in range(int(sys.stdin.readline())):
    print(sum(map(int,sys.stdin.readline().split())))