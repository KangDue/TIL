#양의 정수를 입력받아 문자열로 변환
def itoa(x):
    #넘겨받은 정수를 0이 되기 전까지 계속 반복
    #1의 자리수부터 끊어서 문자열로 변환

    #넘겨받은 값이 음수면 음수 반환
    temp = "" if x > 0 else "-"
    x = abs(x)
    while x:
        temp += chr(ord(chr(x%10)))
        x //= 10
    return temp
print(itoa(-34567))