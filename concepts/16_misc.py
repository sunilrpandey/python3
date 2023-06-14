import itertools

# map - map(iterable_sequence, callback) apply callback on all element and return the transformed container
# When iter() function is called on an Iterable object, it returns an Iterator

#TODO
# make a class iterator
# yield , like return values but does not return 
# Generator, like an iterator for functin etc which generates yields


def demo_use_iter_only_once():
    print("Demo : use iterators more than once") 
    reversed_list = reversed(range(5, 15, 2))
    for i in reversed_list:
        print(i, end = "  ")
    print()
    # it does not print anything in below loop
    for j in reversed_list:
        print(j, end = "  ")
    print()

    # you can use itertools' tee function to create copy of iterators
    r_list = reversed(range(5, 15, 2))
    it1, it2 = itertools.tee(r_list,2)

    for j in it1:
        print(j, end = "  ")
    print()
    
    for j in it2:
        print(j, end = "  ")
    print() 

def demo_looping_techniques_for_containers():

    print("Demo : iterate through containers") 
    
    # enumerate is done on keys in dict, where keys would be 0,1,2 and values would be keys of dictionary
    d2 = {"one": 1, "two": 2, "three": 3}
    for k, v in enumerate(d2):
        print(k, v, end=" , ")
    print()

    
    # for list values would be list of items
    l = [10, 20, 30, 40]
    for k, v in enumerate(l):
        print(k, v, sep="->", end=" , ")
    print()
    
    print("Iterate using list comprehension..")
    [print(i, end="  ") for i in l]
    print()

    # create key value pair from two list
    print("Zipping two list to create dictionary..")
    keys = [1, 2, 3]
    values = ["one", "two", "three"]
    for k, v in zip(keys, values):
        print(k, v, end=" , ")
    print()

    # sort the list
    print("Sorted values : ", sorted(values))

    # reversed range
    for i in reversed(range(5)):
        print(i, end="  ")
    print()

    # reversed range, beg, eng, steps
    # and create list of such entries
    reversed_list = []
    for i in reversed(range(5, 15, 2)):
        reversed_list.append(i)

    print(reversed_list)
    print()

def demo_var_assignment():
    a, b = 3, 5
    print("a = {}, b = {}".format(a, b))

    # c , d = 1,23,45 # error, too many parameters

    b, a = a, b
    print("a = {}, b = {}".format(a, b))

    username, service_provider = "abc.def@gmail.com".split("@")
    print("username = {},service_provider = {}".format(username, service_provider))

def demo_iterable_sequences():
    l1 = ["One","Two","Three"]
    l2 = [1,2,3]

    merged_list = list(itertools.chain(l1,l2))
    print(merged_list)

def demo_map_func_on_iterable_sequence():
    
    print("Multiply each element of the list by 2")
    multiplier_by_2 = lambda x: x * 2
    lst = [1,2,3,4,5,6]
    lst = list(map(multiplier_by_2,lst))
    print(lst)

    print("Join 2 list using map, will work for common nunber of elements")
    l1 = [1,2,3,4,5]
    l2 = ["one", "two", "three", "four"]
    join_func = lambda x, y : str(x) + "_" + y 
    joint_list = list(map(join_func,l1,l2))
    print("Joint list : ", joint_list)

    d = {"one": 1, "two" : 2, "three" : 3}
    dict_mult_2 = lambda x : (x[0], x[1] * 2) # as d.items() returns list of tuples
    d = dict(map(dict_mult_2, d.items()))
    print("Dict with doubled values : ",d)   

def demo_filter_list_of_numbers_for_odd_nums():
    # Program to filter out only the even items from a list
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: (x % 2 != 0), my_list))
    print("list of odd numbers : ", new_list)

def demo_max():
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    print("max value of list :", max(my_list))

    lst = ["Two", "Nine", "Eight"]
    print("Max (Default is alphabetical order) : ", max(lst))
    mx_criteria = lambda x : len(x)
    print("Max (Make string length as criteria) : ", max(lst, key=mx_criteria))

    d = {"Two":2, "Nine":9, "Eight":8}
    print("Max (value in k/v as criteria) : ", max(d.items(), key=lambda x : x[1]))
    
def demo_min():
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    print("min value of list :", min(my_list))

    lst = ["Two", "Nine", "Eight"]
    print("Min (Default is alphabetical order) : ", min(lst))
    min_criteria = lambda x : len(x)
    print("Min (Make string length as criteria) : ", min(lst, key=min_criteria))

    d = {"Two":2, "Nine":9, "Eight":8}
    print("Min (value in k/v as criteria) : ", min(d.items(), key=lambda x : x[1]))

def demo_iter_func():
    l = [1,2,3,4,5]
    l_iter = iter(l)
    print("Type of iterator for list : ", type(l_iter))
    while True:
        try:
            elem = next(l_iter)
            print(elem, end=" - ") 
        except StopIteration:
            break

    print()

if __name__ == "__main__":
    demo_use_iter_only_once()
    # demo_looping_techniques_for_containers()
    # demo_var_assignment()
    # demo_iterable_sequences()
    # demo_map_func_on_iterable_sequence()
    # demo_filter_list_of_numbers_for_odd_nums()
    # demo_max()
    # demo_min()
    # demo_iter_func()