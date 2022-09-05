import sys
sys.stdin = open('input.txt')
import sys
read = sys.stdin.readline
text = read().rstrip()
a = ''
for i in text:
    if i.isupper(): a += i.lower()
    else: a += i.upper()
print(a)