



# Output:
# name: Alice
# age: 30
# city: New York
        
        
def demo_unpacking():
    a, b, c = [5, 10, 15] # works with tuple too
    print(a, b, c)  # Output: 5 10 15

    a, b, *c = [5, 10, 15, 30,50] 
    print(a, b, c)  # Output: 5 10 [15, 30, 50]

    *a, b, c = [5, 10, 15, 30,50] 
    print(a, b, c)  # Output: [5, 10, 15] 30 50

    _, *b, c = [5, 10, 15, 30,50]
    print(b, c)  # Output: [10, 15, 30] 50

    data  = ("Hello",("World", 42))
    a, (b, c) = data
    print(a, b, c)  # Output: Hello World 42

def demo_func_argument_unpacking():
    def print_items(*args):
        for item in args:
            print(item)

        lst = [1, 2, 3, 4, 5]
        print_items(*lst) # Output: 1 2 3 4 5

    def print_dict_items(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    data = {"name": "Alice", "age": 30, "city": "New York"}
    print_dict_items(**data)
    
def demo_list_and_dict_unpacking():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    combined_list = [*lst1, *lst2]
    print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]  
    
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    combined_dict = {**dict1, **dict2}
    print(combined_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
