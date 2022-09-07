import sys
sys.stdin = open('input.txt')
from collections import defaultdict
info = defaultdict(int)
text = input().lower()
for i in text:
    info[i] += 1
val_list = [info[i] for i in info.keys()]
key_list = [i for i in info.keys()]
if val_list.count(max(val_list)) > 1:
    print('?')
else:
    print(key_list[val_list.index(max(val_list))].upper())