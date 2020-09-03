def demo_dictionary_creation():
    empty_dict = dict()
    print(empty_dict)

    dict1 = dict()
    dict1[1] = "one"
    print(dict1)

    d2 = {"one": 1,"two":2,"three":3}
    print(d2)

    d2["four"] = 4
    print(d2)

    for k,v in d2.items():
        print(k,v, sep = "->", end = ",")

    print("\nDict from Arbibrary numbers in tuple")
    d3 = {x : x**2 for x in (2,3,4)}
    print(d3)

    print("only if key is simple string")
    d4 = dict(eleven=11, twelve=12,thirteen=13)
    print(d4)

    print("construct dict from sequence of key-value pair")
    d5 = dict([("one" , 1),("two" , 2),("three" , 3),("ten" , 10)])
    print(d5)

    for k,v in enumerate(d5):
        print(k,v)



def demo_dictionary_operations():
    d = {"one": 1,"two":2,"three":3}
    print(d)
    
    for k,v in d.items():
        print(k,v, sep = "->", end = ",")

    print("\n")
    del d["two"]
    print(d)
    
    d["four"] = 4
    d["five"] = 5

    sorted_list_from_dict = sorted(d)
    print("sorted key list from dict -> ", sorted_list_from_dict)

    keys = d.keys()
    print("keys -> ", keys)
    values = d.values()
    print("values -> , ", values)

    # check if any key is present in dictionary
    print("four" in d)
    print("two" in d)
    print("seven" not in d)
    
    
def demo_looping_techniques_for_containers():
    
    d2 = {"one": 1,"two":2,"three":3}
    for k,v in enumerate(d2):
        print(k,v, end = " , ")
    print("\n")

    # create key value pair from two list
    keys = [1,2,3]
    values = ["one","two","three"]
    for k,v in zip(keys,values):
        print(k,v, end = " , ")
    print("\n")

    # sort the list
    print("sorted values : ", sorted(values))

    # reversed range
    for i in reversed(range(5)):
        print(i, end = "  ")
    print("\n")

    # reversed range, beg, eng, steps
    # and create list of such entries
    reversed_list = []
    for i in reversed(range(5,15,2)):
        reversed_list.append(i)
    
    print(reversed_list)
    print("\n")







# ==== demos
#demo_dictionary_creation()
demo_dictionary_operations()
# demo_looping_techniques_for_containers()

