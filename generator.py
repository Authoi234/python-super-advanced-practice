def foo():
    x=1
    yield x
    x+=1
    yield x
    x+=2
    yield x

def my_range(n):
    x=0
    while x < n:
        yield x
        x += 1

if __name__ == "__main__":
    for i in foo():
        print(i)

    my_range_gen = my_range(5)
    for i in my_range_gen:
        print(i)