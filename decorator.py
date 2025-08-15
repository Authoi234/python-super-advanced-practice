def deco(fnc):
    def wrapper(*args, **kwargs):
        print("before")
        fnc()
        print("after")

    return wrapper

@deco
def hello():
    print("Hello")

# @deco
# def hello_name(name):
#     print("Hello", name)

# @deco
# def add(n1,n2):
#     print(n1+n2)

hello()
print()
# hello_name("World")     """ Error """
print()
# add(3,6)                """ Error """