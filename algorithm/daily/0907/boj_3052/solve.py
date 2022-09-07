import sys
sys.stdin = open('input.txt')
rems = set()
for i in range(10):
    rems.add(int(input())%42)
print(len(rems))