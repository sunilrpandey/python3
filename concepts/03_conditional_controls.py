# nested if/else , for/while loop also works
def demo_while_if_else():
    print("Given number to compare : ")

    given_number = int(input())

    while True:

        test_number = int(input())

        if test_number < given_number:
            print("Less")
        elif test_number > given_number:
            print("More")
        else:
            print("Equal")
            break


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def demo_recursive_function():
    print("Enter number to compute factorial : ", end=" ")
    num = int(input())
    print("Factorial of {} : {}".format(num, factorial(num)))


def demo_for_loop():
    print("Enter number to write mult table : ", end=" ")
    #num = int(input())
    num = 5
    for i in range(11):
        if i == 0:  # works without () too
            continue
        print(num * i)

    print("Iterate through string using two steps..")
    s = "Honesty is the best policy"
    for elem in s[::2]:
        print(elem, end = ",")
    print()

    print("Demo backward iteration...")
    for elem in s[::-1]:
        print(elem, end = "")
    print()
    print("..backward step by 2")
    s = [1,2,3,4,5,6,7,8,9]
    for elem in s[::-2]:
        print(elem, end = " ")
    print()





def demo_nested_for_loop():
    print("Enter range to write multiplication table : ", end=" ")
    start = int(input())
    end = int(input())

    print("Here is multiplication table from {} to {}".format(start, end), end="\n\n")
    for r in range(10):
        for c in range(start, end + 1):
            print("%3d" % (c * (r + 1)), end="  |  ")
        print("\n")

if __name__ == "__main__":
    demo_while_if_else()
    demo_recursive_function()
    demo_for_loop()
    demo_nested_for_loop()

    
