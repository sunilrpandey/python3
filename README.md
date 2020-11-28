# Notes
## Misc Funcs/Concepts
### dir(obj) 
Returns all properties and methods of the specified object, without the values
obj can be struct function or any other object, or even can be empty 
```py
    number = [1, 2, 3]
    print(dir(number))

    print(dir())  # also valid
```

## Python tools
- pylint : install using pip/pip3
- black : install using pip/pip3 // for formatting
### Useful VS Code extension
- pylance
- bookmarks

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
    demo_math()
    demo_math()
    
def pass_func_as_arg_toprint(f, msg):
    f(msg)
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
* Element of list can be homogeneous/hetrogeneous
* Can access list items through indexes
* list is mutable so can replace one item by another
* has 'in' and 'not in' operator
* can iterate thorugh range(n), i.e. 0 to n-1
### List creation and access
```python
    list_is_seq = [10,23,45,67]
    print ("Element of list can be homogeneous as : ",list_is_seq)

    list_hetro = [10,23.5,"No Error",[10,20]]
    print ("..OR it can be mixed as : ",list_hetro)

    print("Iterate thorugh list element")
    for item in list_hetro :
        print(item, end = "  ")

    print("Access list element through Indexes, e.g index 3 is list : ", list_hetro[3])
    print("..and its second element is : ", list_hetro[3][1])

    list_hetro[2] = [1,2]
    print("List is mutable, replacing string at 2 to list : ", list_hetro)

    print("Verify if [1,2] is in the list ? : ", [1,2] in list_hetro)
    print("Verify if 23.5 is in the list ? : ", 23.5 in list_hetro)
    print("Verify if 235 is in the list ? (Should be false): ", 235 in list_hetro)

    print("\nIterate thorugh element indexes")
    for idx in range(len(list_hetro)) :
        print(list_hetro[idx], end = "  ")
```
### Various List Operations
Most list methods modifies the argument and return None . This is the opposite of the string methods, which return a new string and leave the original alone.

* count(item) gives frequency of 'item' in the list
* len(list) gives number of items in the list
* Use reverse, min, max, len
* del list[id], id can be index or slice syntaxes as well 
* list.remove(item), takes item as argument not index
* index(item), insert, pop(index),pop(), remove(item), sort, sum
* append(new_item), extend(new_list)
* list1 + list to add two list, list * num to multiply list items 
* slice works similar to string
* append/extend modifies the list whereas + operator creates new list
* slice also creates a new list

```python
    mylist1 = [10,20,30]
    mylist1.reverse()
    print(mylist1)
    
    mylist = [10,20,30]
    
    mylist.insert(-2,40) # [10, 40, 20, 30] // place at index 2 from last
    mylist.insert(1,400) # [10, 400, 40, 20, 30]
    print(mylist)
    print("Max = ", max(mylist)) #max element
    print("Min = ", min(mylist)) #min element
    print("Length = ", len(mylist)) # number of element
    print("Inded of 20 = ", mylist.index(20))
    print("Element at 3 removed : ", mylist.pop(3)) # 20 is popped
    print("Last Element : ", mylist.pop()) # 30 is popped
    print("Now mylist is : ", mylist)
    print("Remove 400 : ")
    mylist.remove(400) # removed
    
    list1 = [1,2,3]
    list2 = [4,5] 
    #print("Comparison : ", cmp(list1,list2))
    print("Twice the list : ", list2 * 2)
        
    sum_list = list2 + list1
    print("sum list (list1 + list2) : ", sum_list)
    
    sum_list.sort()
    print("sort list : ", sum_list)

    print("sum of sorted list : ", sum(sum_list))

    list3 = [6, ["Happy ","Coding", 2.0]]

    sum_list = sum_list + list3
    print("sum of different lists", sum_list)

    list4 = [1,2]
    print("Same items get multiplied in case of multiplication, wil print [1,2,1,2] : ", list4 * 2)

    # slice works similar to string
    list4.append(3) # this does not return list
    print("append method updates itself but does not return list : ", list4)

    list4.extend(list1) # this also does not return list
    print("extend function updates itself but does not return list : ", list4.extend(list1))
```
Adding few more 
```python
    list1 = [1,2,3]
    list2 = [4,5]

    sum_list = list2 + list1
    print("sum list2 + list1 : ", sum_list)

    print("Pop top element", sum_list.pop()) # returns top element
    print("updated sum_list", sum_list)

    del sum_list[1] # slicing can be used
    print("Deletes index 1 element(i.e. 5) : ", sum_list)

    sum_list.remove(1) #takes element as argument
    print("list after removing 1 : ", sum_list)
```
### String, list and comparisons
* string to list
* is operator

```python
    a = "Hello-Python"
    list_a = list(a)
    print("list func convert string into list individual chars : ", list_a)           #[H,e,l,l.....]
    print("string func split converts gives list of words : ", a.split(sep = "-"))    # [Hello, Python]

    a = "Hello"
    b = "Hello"
    print("Both points to same string so are equal/identical : ", a is b) 
    
    a = [1,2]
    b = [1,2]
    print("Both are equivalent but not equal/identical : ", a is b) 

    c = a 
    print("Aliased, Both are equal/identical : ", c is a) 
    
    a[1] = 10
    print("As second element of a got modified, c will change too : ", c)
``` 