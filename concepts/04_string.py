import os
import sys

# learning : ref string func
# https://www.programiz.com/python-programming/methods/string/endswith


def demo_str_2_list():
    str = "Honesty is the best policy"

    print(str, len(str), sep="  :    ")

    list_word = str.split(sep=" ")
    print("List of words in quote : ", list_word)

    for word in list_word:
        print(word, end="_")


def demo_slices():
    print("Demo string slices and access me")
    str = "Hello World"  
    print("Last letter :", str[-1])
    print("Second Last letter :", str[-2])
    
    print("First 7 : ", str[0:7])
    print("Last 4 : ", str[-4:])
    print("First 3 : ", str[:3])
    print("third onward : ", str[3:])
    print("Effectively None : ", str[3:3])
    
    try :
        print(str[20])
    except IndexError:
        print("Index : out of range!!")



def demo_immutable_string():
    str = "Hello Python"
    # str[0] = 'J'       # can not change immutable string

    modified_str = "J" + str[1:]
    print(modified_str)


def demo_string_func():
    str = "Hello Python"
    print("Capitalize : ", "hello world".capitalize())
    print("Count : ", str.count("l", 0, len(str)))
    print("length of string is : ", len(str))
    print("string in upper case ", str.upper())
    print("lstrip demo:", "44444      Hello World!!!!!!!".lstrip("4"))
    print("rstrip demo:", "44444      Hello World!!!!!!!".rstrip("!"))
    print("Index of P : ", str.index("P"))
    print("Index of Python : ", str.find("Python"))
    print("Check if string has e : ", "e" in str)
    print("Check if string has a : ", "a" in str)
    print("Check if string has 'Python' : ", "Python" in str)

    first_word = str.split(sep=" ")[0]
    if first_word == "Hello":
        print("First word of string is : ", first_word)

    if first_word < "Python":
        print("String comparison based on alphabtical order")


def demo_words_in_string():
    l = ["is", "best"]
    s = "Honesty is the best policy"

    found = all([True if word in s else False for word in l])
    if found:
        print("All words in list are part of string")

    #l = ["are", "is", "best"]
    l = ["aare", "ais", "abest"]
    s = "Honesty is the best policy"
    found = any([True if word in s else False for word in l])
    if found:
        print("At leaset one word in list is part of string")
    else:
        print("None of words in list is part of string")

def reverse(str):
    return str[::-1]

def isPalindrome(str):
    return str == reverse(str)
        
    

if __name__ == "__main__":
    # print(reverse("anystring"))
    # print(isPalindrome("madam"))
    
    # demo_str_2_list()
    # demo_slices()
    # demo_string_func()
    # demo_immutable_string()

    demo_words_in_string()
    