# Notes

## Print Statements
Enters space "  " after print instead of new line
> print("Hello Python 3!!",end="  ") 

Print a value (new line) 5 times
> print("\n" * 5)

Substitute operator uses {}.format 
> print("first_name {}".format(a))

Prints separator 
> print(a,b, sep=' : ') 

## Functions
```python
def reuse_fun(message):
    print(message)
    demo_math();
    demo_math();
    
def pass_func_as_arg_toprint(f, msg):
    f(msg);
```
Python have conditional control, recursion, nested loop, break/continue etc
```python
def demo_while_if_else():
    print("Given number to compare : ")

    given_number = int(input())

    while True :
        
        test_number = int(input())

        if(test_number < given_number) :
            print("Less")
        elif(test_number > given_number) :
            print("More")
        else  : 
            print ("Equal")
            break

def factorial(n):
    if(n == 1) :
        return 1
    else :
        return n * factorial(n-1)
```
## String

### String to list
```python
str = "Honesty is the best policy"
list_words = str.split(sep=" ")    
```
### String Slices
```python
def demo_slices():
    str = "Hello World"
    print("First 7 : ",str[0:7])                # Hello W
    print("Last 4 : ", str[-4:])                # orld
    print("First 3 : ", str[:3])                # Hel
    print("third onward : ", str[3:])           # lo World
    print("Effectively None : ", str[3:3])      # "" i.e empty string
```
### Mutable Strings
```python
def demo_immutable_string():
    str = "Hello Python"
    #str[0] = 'J'       # can not change immutable string

    modified_str = 'J' + str[1:]
    print(modified_str)
```
### String Functions
```python
def demo_string_func():
    str =  "Hello Python"
    print("Capitalize first letter of each word: ", "hello world".capitalize()) # Hello World
    print("Count of char c: ", str.count("l", 0, len(str)))                     # 2
    print("length of string is : ", len(str))
    print("string in upper case ", str.upper())                                 # all upper case
    print("lstrip demo:", "44444      Hello World!!!!!!!".lstrip('4'))          # all 4 and space
    print("rstrip demo:", "44444      Hello World!!!!!!!".rstrip('!'))          # all ! and space
    print("Index of P : ", str.index('P'))
    print("Index of Python : ", str.find("Python"))
    print("Check if string has e : ", 'e' in str)                   # True
    print("Check if string has a : ", 'a' in str)                   # False
    print("Check if string has 'Python' : ", "Python" in str)       # True

    first_word = str.split(sep=" ")[0]      # Will give list of words, 0 index will give first word of it
    if(first_word == "Hello"):
        print("First word of string is : ", first_word)

    if(first_word < "Python"):
        print("String comparison based on alphabtical order")
```
## List