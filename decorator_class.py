class DecoratorClass:
    def __init__(self, fnc):
        self.fnc = fnc
    def __call__(self, *args, **kwargs):
        print("before")
        self.fnc(*args, **kwargs)
        print("after")

@DecoratorClass
def hello():
    print("Hello")

@DecoratorClass
def hello_name(name):
    print("Hello", name)

hello()
print()
hello_name("Python")