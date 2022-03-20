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
    pass

d = D(1, 2, 3)
print(isinstance(d, A),isinstance(d, B),isinstance(d, C))
print(d.a, d.b, d.c)