# write a generator function for count_upto(maxvalue)
def count_upto(maxvalue):
    for i in range(maxvalue):
        yield i
        
# write a demo function to show how to use count_upto
def count_upto_demo():
    print("Count Upto Demo: Using a generator to count up to a maximum value")
    for i in count_upto(5):
        print(i, end=' ')
    print()

    print("Using the generator directly:")
    counter = count_upto(5)
    print(next(counter))  # Get the next value from the generator
    print(next(counter))  # Get the next value from the generator
    
if __name__ == "__main__":
    count_upto_demo()
    