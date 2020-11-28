def demo_dictionary_creation():
    # create empty dict
    empty_dict = dict()
    print(empty_dict)

    # ..and add entry
    dict1 = dict()
    dict1[1] = "one"
    print(dict1)

    # create with initialized key values
    d2 = {"one": 1, "two": 2, "three": 3}
    print(d2)

    # add to already initialized dict
    d2["four"] = 4
    print(d2)

    ## Iterate through dict items, separtor and eol customized
    for k, v in d2.items():
        print(k, v, sep="->", end=",")

    print("\nDict from Arbibrary numbers in tuple")
    d3 = {x: x ** 2 for x in (2, 3, 4)}
    print(d3)

    print("only if key is simple string")
    d4 = dict(eleven=11, twelve=12, thirteen=13)
    print(d4)

    print("construct dict from sequence of key-value pair")
    d5 = dict([("one", 1), ("two", 2), ("three", 3), ("ten", 10)])
    print(d5)

    for k, v in enumerate(d5):
        print(k, v)  # will enumerate keyes i.e. 0 : key1, 1 : key2 etc

    return


def demo_dictionary_operations():

    # using print to view dict items
    d = {"one": 1, "two": 2, "three": 3}
    print(d)

    # iterate through keysto print keys
    print("keys : ")
    for k in d.keys():
        print(k, end=",")
    print()

    # iterate through valuesto print values
    print("values : ")
    for v in d.values():
        print(v, end=",")
    print()

    # iterate through  key/values to print items
    print("items in dictionary : ")
    for k, v in d.items():
        print(k, v, sep="->", end=",")
    print()

    # delete item using key
    del d["two"]
    print("deletes key 'two'", d)

    # add items using index of [] operator
    print("Add two four/five keys")
    d["four"] = 4
    d["five"] = 5

    # use sorted method on keys to sort items
    sorted_list_from_dict = sorted(d)
    print("sorted key list from dict -> ", sorted_list_from_dict)

    keys = d.keys()
    print(
        "keys as dict_keys -> ", keys
    )  # will output dict_keys(['one', 'three', 'four', 'five'])
    print("keys as list only -> ", list(d.keys()))
    values = d.values()
    print("values as dict_keys-> ", values)
    print("values as list only -> ", list(values))

    # check if any key is present in dictionary
    print("Four in Dict? : ", "four" in d)
    print("two in Dict? : ", "two" in d)
    print("seven not in Dict? : ", "seven" not in d)


def demo_looping_techniques_for_containers():

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


# ==== demos
# demo_dictionary_creation()
# demo_dictionary_operations()
demo_looping_techniques_for_containers()
