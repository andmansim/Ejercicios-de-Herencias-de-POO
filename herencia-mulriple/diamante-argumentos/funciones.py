from mimetypes import init


class A:
    def __init__(self, a):
        self.a = a

class B(class A):
    def __init__(self, a, b):
        class A.__init__(self, a)
        self.b = B
