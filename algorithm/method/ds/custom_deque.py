class Deque:
    F = None
    B = None
    def __init__(self,value,front=None,back=None):
        self.value = value
        self.front = front
        self.back = back
    @classmethod
    def push_front(cls,other):
        other = Deque(other)
        if cls.F:
            other.back, cls.F = cls.F, other
            other.back.front = other
        else:
            other.back, cls.F = cls.F, other
        p = cls.F
        while p.back:
            p = p.back
        cls.B = p

    @classmethod
    def push_back(cls,other):
        other = Deque(other)
        if cls.B:
            other.front, cls.B = cls.B, other
            other.front.back = other
        else:
            other.front, cls.B = cls.B, other
        p = cls.B
        while p.front:
            p = p.front
        cls.F = p
    @classmethod
    def pop_front(cls):
        if cls.F:
            print(cls.F.value)
            if cls.F.back:
                cls.F = cls.F.back
                cls.F.front = None
            else:
                cls.F = cls.B = None
        else:
            print(-1)
    @classmethod
    def pop_back(cls):
        if cls.B:
            print(cls.B.value)
            if cls.B.front:
                cls.B = cls.B.front
                cls.B.back = None
            else:
                cls.B = cls.F = None
        else:
            print(-1)
    @classmethod
    def size(cls):
        c = 0
        p = cls.F
        while p:
            p = p.back
            c += 1
        print(c)
    @classmethod
    def empty(cls):
        print(+(cls.F == cls.B == None))
    @classmethod
    def front(cls):
        if cls.F:
            print(cls.F.value)
        else:
            print(-1)
    @classmethod
    def back(cls):
        if cls.B:
            print(cls.B.value)
        else:
            print(-1)