class Stack:
    def __init__(self,max_size = 0):
        self.max_size = max_size
        self.arr = [None]*self.max_size #처음 크기 생성시 값이 없어야 하므로 None
        self.top = -1 # 아무것도 없는 상태니까

    def push(self,x):
        try:
            self.top += 1
            self.arr[self.top] = x
        except:
            self.top -= 1
            print(f"스택이 가득차서 더 이상 {x}를 추가할 수 없습니다.")
    def pop(self):
        if self.top == -1:
            print("스택이 비어서 더 이상 제거할 수 없습니다.")
        else:
            temp = self.arr[self.top]
            self.top -= 1
            return temp

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.max_size -1 :
            return True
        else:
            return False
a = Stack(3)
print("비었니?",a.is_empty())
a.pop()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print(a.arr)
print("꽉찻니?",a.is_full())
print(a.pop())
print("꽉찻니?",a.is_full())
print("비었니?",a.is_empty())
