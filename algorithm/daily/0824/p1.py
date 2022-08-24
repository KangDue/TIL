class Lqueue:
    def __init__(self):
        self.front =- 1
        self.rear =- 1
        self.arr=[]
    def isFull(self):
        return self.rear == self.size-1
    def isEmpty(self):
        return self.front == self.rear
    def enqueue(self,x):
        self.rear += 1
        self.arr.append(x)
    def dequeue(self):
        self.front += 1
        return self.arr[self.front]
if __name__=='__main__':
    a = Lqueue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())