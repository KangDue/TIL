import sys
sys.stdin = open('input.txt')
def is_pal(arr):
    if len(arr) <= 1:
        return True
    elif arr[0] != arr[-1]:
        return False
    else:
        return is_pal(arr[1:-1])
while 1:
    text = input()
    if text == '0': break
    if is_pal(text): print('yes')
    else: print('no')
