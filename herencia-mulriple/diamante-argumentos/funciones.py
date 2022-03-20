class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b
        
class C(A):
    def __init__(self, a, c):
        super.__init__()
        self.c = c

class D(B, C):
    def __init__(self, b, c, d):
        super.__init__()
        self.d = d