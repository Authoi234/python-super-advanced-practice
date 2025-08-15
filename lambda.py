def addition(n1):
    return lambda n2: n1 + n2

if __name__ == "__main__":
    one_plus = addition(1)
    print(one_plus(10)) 