# Notes

## TODO:
reduce n accumulate

## Misc Funcs/Concepts
- () around if/for/while is optional
- .split(delimiter) - returns list based on delimeter
- reversed(list) returns listiter object not list itself, so iterate to read values
- append adds individual elm or list(whole), extend adds individual elem of list to target list
- for k, v in d2.items():
        print(k, v, sep="->", end=",")
- dict = {x: x ** 2 for x in (2, 3, 4)}
- set : unordered collection of unique element, {}
- for loop for range(for i in list), while uses in operator
- In Set order can change as it is not  
- reverse of list is list[::-1]
- lst.sort(reverse=True, key=int) // specify list has integer in form of string
- merge list using extend,append,iterate or itertools.chain
- len(2d_list) or list of list will return number of lists, to know number of item iterate through or recursively these lists, or hetrogenous lists
- type(elem) == list, to check if elem is list
- map(lambda x : x%2 == 1, lst) //lambda applies on each elemnt of lst

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

> print(f"Let us celebrate {year} {event}")
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
Python has conditional control, recursion, nested loop, break/continue etc
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
    print("Last 5th to last 1st", str[-5:-1])   # Worl
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
    print("length of string is : ", len(str))
    print("string in upper case ", str.upper())                                 # all upper case
    
    print("Count of char c: ", str.count("l", 0, len(str)))                     # 2
    print("lstrip demo:", "44444      Hello World!!!!!!!".lstrip('4'))          # all 4 from left till other char starts
    print("rstrip demo:", "44444      Hello World!!!!!!!".rstrip('!'))          # all ! from the right till other char starts
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
* search item in list using in/not in operator, list.count(item) returns number of itme in list

Most list methods modifies the argument and return None . This is the opposite of the string methods, which return a new string and leave the original alone.

### List creation and access
```python
    lst = [] # empty list
    print(lst)

    lst = ["Hello"] * 5 #[ 'Hello', 'Hello', 'Hello', 'Hello', 'Hello']
    print(lst)

    lst = ["World" for i in range(5)] # ['World', 'World', 'World', 'World', 'World']
    print(lst)

    list_is_seq = [10,23,45,67]
    print ("Element of list can be homogeneous as : ",list_is_seq)

    list_hetro = [10,23.5,"No Error",[10,20]]
    print ("..OR it can be mixed as : ",list_hetro)

    print("Iterate thorugh list element")
    for item in list_hetro :
        print(item, end = "  ")

    print("Access list element through Indexes, e.g elem at index 3 is list : ", list_hetro[3])
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
* index(item), insert, pop(index), pop(), remove(item), sort, sum
* append(new_item), extend(new_list)
* list1 + list to add two list, list * num to multiply list items 
* slice works similar to string
* append/extend modifies the list whereas + operator creates new list
* slice also creates a new list

* new_list = lst[start:stop:step] e.g. reversed_list = lst[::-1]
* In list remove uses item where as del  uses index
* Delete last element, del lst[-1]

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

    another_list = [4,5]
    list4.append(another_list) # will output [1,2,3,[4,5]] not [1,2,3,4,5]
    print("append adds whole list not individual elem : ", list4)
    
    lst_to_extend = [6,7]
    list4.extend(lst_to_extend) # this does not return list but adds 6, 7 to existing list make list4 = [1, 2, 3, [4, 5], 6, 7]
    print(list4)
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

## Dictionary
Iterate through dict items, separtor and eol customized
```py
    for k, v in d2.items():
        print(k, v, sep="->", end=",")
``` 
Dictionaries have keys() values() and items() to get keys, values and key-value pairs.
but get list of keys/values do it explicitely e.g. list(dict.keys()) 

Check if key availabe using 
  - key in dict
  - key in keys
  - d[key] is 'KeyError'
### sorted()
dict = sorted(dict) to sort dictionary(on keys) or other containers e.g. list and tuples 

## Set
Unordered collection of unique element, {},  It provides various set relatd operations
```python
    s1 = set("test")
    print("s1 (test) -> ", s1) # will outpu {'t', 's', 'e'}

    s2 = set("Taste")
    print("s2 (Taste) -> ", s2) # will output {'s', 't', 'a', 'e', 'T'}

    print("s1 - s2 -> ", s1 - s2)  # in s1 but not in s2
    print("s2 - s1 -> ", s2 - s1)  # in s2 but not in s1
    print("s1 | s2 -> ", s1 | s2)  # in s1 or s2
    print("s1 & s2 -> ", s1 & s2)  # both in s1 and s2
    print("s1 ^ s2 -> ", s1 ^ s2)  # in s1 or s2 but not in both
```
## Tuple
A tuple is a sequence of values. The values can be any type, and they are indexed by integers, so in that respect tuples are a lot like lists.
The important difference is that tuples are immutable.

zip is a built-in function that takes two or more sequences and “zips” them into a list of tuples where each tuple contains one element from each sequence.
In Python 3, zip returns an iterator of tuples, but for most purposes, an iterator behaves like a list.

Tuple supports functions such as sort, compare operators(compares begining to end)
### Creations 
```py
    empty_tuple = tuple()
    print("empty tuple -> ", empty_tuple)

    t = "a", "b", "c", "d", "e"
    print("tuple from values -> ", t)

    # or represent it using (better)
    t1 = ("a", "b", "c", "d", "e")
    print("tuple from values -> ", t1)

    # string to tuple elements
    t2 = tuple("abrakadabra")
    print("tuple elements from t2 -> ", t2) # it allows duplicates as well

    # access method is same as list i.e. 0 based l;
    print("t2[0] -> {}\nt2[3:6] -> {}".format(t2[0], t2[3:6]))

    # you can not modify tuple elements but can replace tuple
    #t3 = t2[0] + t2[3:6] # not working, says can not concatanate
    t2 = ("A",) + t2[3:6] # please do notice , after "A"
    print("relaced tuple(t2) - > ", t2)
```

# Variable scope
### global 
It can be read from the code but if you want to update you have to declare locally
    global x
global is not required if it is mutable such as list, dictioanary and sets
### nonlocal
Basically used for nested function, need to declare locally if variable is defined in outer nested function.
Local/nonlocal variable will get precedence over global one
```py
spam = "temp"
def demo_scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
        #print(spam) # will print updated value here only

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
```
Outside demo_scope_test, its modified global value that would be available, verify it using 
```py
    print("In global scope:", spam) # will print "global spam" modified by do_global function
```

# More about file handling
Check if file is empty
``` 
os.stat(path, *, dir_fd=None, follow_symlinks=True)
os.stat(file_path).st_size == 0 to check if file is empty
os.path.getsize(path)
fileStatsObj = os.stat ( filePath )
modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
accessTime = time.ctime ( fileStatsObj [ stat.ST_ATIME ] )
os.path.getmtime(path)

modificationTime = time.strftime('%d/%m/%Y', time.localtime(os.path.getmtime(filePath)))
accessTimesinceEpoc = os.path.getatime(filePath)
accessTime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(accessTimesinceEpoc))


#open file and read first char
one_char = read_obj.read(1)
# if not fetched then file is empty
if not one_char:
    return True
```