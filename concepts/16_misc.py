import itertools

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

    # create key value pair from two list
    keys = [1, 2, 3]
    values = ["one", "two", "three"]
    for k, v in zip(keys, values):
        print(k, v, end=" , ")
    print("\n")

    # sort the list
    print("sorted values : ", sorted(values))

    # reversed range
    for i in reversed(range(5)):
        print(i, end="  ")
    print("\n")

    # reversed range, beg, eng, steps
    # and create list of such entries
    reversed_list = []
    for i in reversed(range(5, 15, 2)):
        reversed_list.append(i)

    print(reversed_list)
    print("\n")

if __name__ == "__main__":
    demo_use_iter_only_once()
    demo_looping_techniques_for_containers()