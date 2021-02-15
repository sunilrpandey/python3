"""This module does blah blah."""
#!usr/bin/env python
import itertools
import json
from collections import Counter 
"""
dict study
"""


def demo_dictionary_creation():
    """function(a, b) -> list"""
    # create empty dict
    print("Empty dict using dict() :")
    empty_dict = dict()
    print(empty_dict)
    another_empty_dict = {}
    print("AnotherEmpty dict using {} :", another_empty_dict)

    # ..and add entry
    empty_dict[1] = "one"
    print("Added '1', No more empty", empty_dict)

    # create with initialized key values
    print("Another way to init d = {k:v}")
    d2 = {"one": 1, "two": 2, "three": 3}
    print(d2)

    print("Add 'four'")
    # add to already initialized dict
    d2["four"] = 4
    print(d2)

    ## Iterate through dict items, separtor and eol customized
    for k, v in d2.items():
        print(k, v, sep="->", end=",")

    print("\nDict from Arbibrary numbers in tuple,x: x ** 2 for x in (2, 3, 4)")
    d3 = {x: x ** 2 for x in (2, 3, 4)}
    print(d3)

    print("Init using dict(k=v,)only if key is simple string")
    d4 = dict(eleven=11, twelve=12, thirteen=13)
    print(d4)

    print("Init from list of tuples,  key-value pair")
    d5 = dict([("one", 1), ("two", 2), ("three", 3), ("ten", 10)])
    print(d5)

    return


def if_key_exist(dict, key):
    """function(a, b) -> list"""
    try:
        value = dict[key]
        return True
    except:
        return False

    # return key in dict
    # return key in dict.keys()
    # or iterate over dictionary and comapare values
    # return dict.get(key) is not None


def if_value_exist(dict, value):
    """function(a, b) -> list"""
    return any([True for k, v in dict.items() if v == value])
    # return value in dict.values()
    # return not value not in dict.values()
    # or iterate over dictionary and comapare values


def demo_dictionary_operations():
    """function(a, b) -> list"""

    print("Demo Dictionary operations")
    # using print to view dict items
    d = {"one": 1, "two": 2, "three": 3}
    print(d)

    # iterate through keysto print keys
    print("Iterate over [List] of keys, keys(): ")
    for k in d.keys():
        print(k, end=",")
    print()

    # iterate through valuesto print values
    print("Iterate over [List] of values, values() : ")
    for v in d.values():
        print(v, end=",")
    print()

    # iterate through  key/values to print items
    print("Items in dictionary, items() : ")
    for k, v in d.items():
        print(k, v, sep="->", end=",")
    print()

    # delete item using key
    print("Delete using key, 'del dict[key]'")
    del d["two"]
    print("deletes key 'two'", d)
    # print("Two still there ? Ans : ", if_key_exist(d,"two"))
    k = "two"
    print("Two still there ? Ans : ", d.get("two", "two") is None)
    print("And Value for two ? Ans : ", if_value_exist(d, 2))
    print("And Key three ? Ans : ", if_key_exist(d, "three"))
    print("And Value for three ? Ans : ", if_value_exist(d, 3))

    # add items using index of [] operatorj
    print("add item, dict[k] = value :")
    print("Add two four/five keys")
    d["four"] = 4
    d["five"] = 5

    # use sorted method on keys to sort items
    print("sorted(d) works on keys : ")
    sorted_list_from_dict = sorted(d)
    print("sorted key list from dict -> ", sorted_list_from_dict)

    keys = d.keys()
    print(
        "keys from dict are in form of dict_keys : ", keys
    )  # will output dict_keys(['one', 'three', 'four', 'five'])
    print(".. and can be cast to list using list(keys) -> ", list(d.keys()))
    values = d.values()
    print("values as dict_values-> ", values)
    print("values as list from list(d.values) -> ", list(values))

    # check if any key is present in dictionary
    print("'in' and 'not in' works for dict keys")
    print("Four in Dict? : ", "four" in d)
    print("two in Dict? : ", "two" in d)
    print("seven not in Dict? : ", "seven" not in d)

    print("List of keys start with f : ", [x for x in d if x.startswith("f")])

    print("Enumerate over keys, idx, key")
    for idx, ky in enumerate(d):
        print(
            "{}-{}".format(idx, ky), end=","
        )  # will enumerate keyes i.e. 0 : key1, 1 : key2 etc

    print()


def filter_dictionary(d, callback):
    """function(a, b) -> list"""
    new_d = {}
    for k, v in d.items():
        if callback((k, v)):
            new_d[k] = v

    return new_d


def demo_filter_dictionary():
    """function(a, b) -> list"""
    d = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
    print("Filering on keys...")
    callback = lambda kv: kv[0] < 4
    new_d = filter_dictionary(d, callback)
    print(new_d)

    print("Filering on values...")
    callback = lambda kv: kv[1].startswith("f")
    new_d = filter_dictionary(d, callback)
    print(new_d)

    print("Filtering using 'filter' method..")
    new_d = dict(filter(lambda kv: kv[0] < 3, d.items()))
    print(new_d)

def demo_json_dump():
    print("Demo : Json repreentation for dict")
    d = {1:'a',2:'b',3:'c'}
    print(json.dumps(d,indent=4))

    print("Demo : Json repreentation for nested dict")
    d = {1:{'a':"abc","b":"def","c":"ghi"},2:{"b":"123","c":"456"},3:"c"}
    print(json.dumps(d,indent=4))
    
def demo_convert_list_to_dict():
    l = [1,2,3,4,2,3,1,4,6,7,8]
    d = {i : "num" for i in l}
    print(d)

    d = dict(Counter(l))
    print(d)

# ==== demos
if __name__ == "__main__":
    """function(a, b) -> list"""
    # demo_dictionary_creation()
    # demo_dictionary_operations()
    # demo_filter_dictionary()
    # demo_json_dump()
    demo_convert_list_to_dict()
    #todemo: zip twolist and then dict(zippedlists)
    #todemo: list of tuples to dict(listoftuples)0
    # sort based on key
    # sort based on value l_tupls = sorted(d.items() , key=lambda x: x[1])
    # sort reverse on keys l_tupls = sorted(d.items() , reverse=True)
    # sort revers on values l_tupls = sorted(d.items() , reverse=True, key=lambda x: x[1])
    # sort based on custom function
    # --- sorted(iterable_seq, custom Function)
    # shall copy -> new_dict = d.copy() this will copy references of non primitive object such as list, dict,tuple so any change in new_dict for list will reflect in original dict ojbect as well
    # deep copy -> import copy --> new_d = copy.deepcopy(orig_d)
