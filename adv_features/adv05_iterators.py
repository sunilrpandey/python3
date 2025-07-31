def range_demo():
    print("Range Demo: Iterating through a range of numbers")
    for i in range(5):
        print(i, end=' ')
    print()

def iter_demo():
    print("Iter Demo: Using an iter/next to go through a range")
    r = range(10)
    itr = iter(r)
    while True:
        try:
            print(next(itr), end=' ')
        except StopIteration:
            break
    print()


class MyRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

    def __iter__(self):
        return self
        
#write a demo function to show how to use MyRange
def my_range_demo():
    print("MyRange Demo: Custom range implementation")
    for i in MyRange(3, 8): # similar to range function
        print(i, end=' ')
    print()

if __name__ == "__main__":
    #range_demo()
    #iter_demo()
    my_range_demo()
    