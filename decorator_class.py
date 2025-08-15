class DecoratorClass:
    def __init__(self, *args):
        pass
    def __call__(self, *args):
        pass

@DecoratorClass
def hello():
    print("Hello")

@DecoratorClass
def hello_name(name):
    print("Hello", name)

hello()
print()
hello_name("Python")