class A:
    def fnc(self):
        print("Hello from A")
    
class B:
    def fnc(self):
        print("Hello from B")

class C(A, B):
    pass

obj = C()
obj.fnc()

class D(B, A):
    pass

obj = D()
obj.fnc()

print(D.mro())
print(C.mro())

#  Diamond problem , Not a problem in Python
class A():
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")

class C(A):
    def hello(self):
        print("Hello from C")

class D(B, C):
    pass

obj = D()
print(obj.hello()) 