class my_range:
    def __init__(self,startIndex=0, n=1, step=1):
        self.index = startIndex
        self.max_index = n-1
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.max_index:
            self.index += self.step
            return self.index - self.step
        else:
            raise StopIteration()

if __name__ == "__main__":
    for i in my_range(5, 10, 2):
        print(i)