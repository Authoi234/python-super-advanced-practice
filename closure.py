def addition(n1):
    def add(n2):
        return n1 + n2
    
    return add

if __name__ == "__main__":
    ten_plus = addition(10)
    hundred_plus = addition(100)

    print(ten_plus(5))
    print(hundred_plus(20))