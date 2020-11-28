# Learnings
# append/extend modifies the list whereas + operator creates new list
# slice also creates a new list

# Don’t forget that most list methods modifies the argument and return None . This is
# the opposite of the string methods, which return a new string and leave the original
# alone.


def demo_list_element_access():
    list_int = list()
    if len(list_int) == 0:
        print("List is Empty!")

    list_int_2 = []
    if len(list_int_2) == 0:
        print("List is Empty!")

    # if we do list_int_2 = list_int, it will be same
    if list_int is list_int_2:
        print("Same")
    else:
        print("Not Same")

    list_is_seq = [10, 23, 45, 67]
    print("Element of list can be homogeneous as : ", list_is_seq)

    list_hetro = [10, 23.5, "No Error", [10, 20]]
    print("..OR it can be mixed as : ", list_hetro)

    print("Iterate thorugh list element")
    for item in list_hetro:
        print(item, end="  ")

    print("Access list element through Indexes, e.g 3 has list : ", list_hetro[3])
    print("..And its second element is : ", list_hetro[3][1])

    list_hetro[2] = [1, 2]
    print("List is mutable, replacing string at 2 to list : ", list_hetro)

    print("Verify if [1,2] is in the list ? : ", [1, 2] in list_hetro)
    print("Verify if 23.5 is in the list ? : ", 23.5 in list_hetro)
    print("Verify if 235 is in the list ? (Should be false): ", 235 in list_hetro)

    print("\nIterate thorugh element indexes")
    for idx in range(len(list_hetro)):
        print(list_hetro[idx], end="  ")

    print("\n")


def demo_list_operations():

    mylist1 = [10, 20, 30]
    mylist1.reverse()
    print(mylist1)

    mylist = [10, 20, 30]

    mylist.insert(-2, 40)  # [10, 40, 20, 30]
    mylist.insert(1, 400)  # [10, 400, 40, 20, 30]
    print(mylist)
    print("Max = ", max(mylist))  # max element
    print("Min = ", min(mylist))  # min element
    print("Length = ", len(mylist))  # number of element
    print("Inded of 20 = ", mylist.index(20))
    print("Element at 3 removed : ", mylist.pop(3))  # 20 is popped
    print("Last Element : ", mylist.pop())  # 30 is popped
    print("Now mylist is : ", mylist)
    print("Remove 400 : ")
    mylist.remove(400)  # removed

    list1 = [1, 2, 3]
    list2 = [4, 5]
    # print("Comparison : ", cmp(list1,list2)) # you need to write cmp function to compare two list
    print("Twice the list : ", list2 * 2)

    sum_list = list2 + list1
    print("sum list (list1 + list2) : ", sum_list)

    sum_list.sort()
    print("sort list : ", sum_list)

    print("sum of sorted list : ", sum(sum_list))

    list3 = [6, ["Happy ", "Coding", 2.0]]

    sum_list = sum_list + list3
    print("adding hetrogenous lists items", sum_list)

    list4 = [1, 2]
    print(
        "Same items get multiplied in case of multiplication, wil print [1,2,1,2] : ",
        list4 * 2,
    )

    # slice works similar to string

    list4.append(3)  # this does not return list
    print("append method updates itself but does not return list : ", list4)

    list4.extend(list1)  # this also does not return list
    print(
        "extend function updates itself but does not return list : ",
        list4.extend(list1),
    )


def demo_list_operations_ex():
    list1 = [1, 2, 3]
    list2 = [4, 5]

    sum_list = list2 + list1
    print("sum list2 + list1 : ", sum_list)

    print("Pop top element", sum_list.pop())  # returns top element
    print("updated sum_list", sum_list)

    del sum_list[1]  # slicing can be used
    print("Delete index 1 element(i.e. 5) : ", sum_list)

    sum_list.remove(1)  # takes element as argument
    print("list after removing 1 : ", sum_list)


def remvoe_element_from_list(lst, id):
    del lst[id]


def demo_string_list_of_char_comparison():
    a = "Hello-Python"
    list_a = list(a)
    print("list func convert string into list individual chars : ", list_a)
    print("string func split converts string into list of words : ", a.split(sep="-"))

    a = "Hello"
    b = "Hello"
    print("Both points to same string so are equal/identical : ", a is b)

    a = [1, 2]
    b = [1, 2]
    print("Both are equivalent but not equal/identical : ", a is b)

    c = a
    print("Aliased, Both are equal/identical : ", c is a)

    a[1] = 10
    print("As second element of a got modified, c will change too : ", c)

    # when  you pass a list to a functio, it is passed by reference
    remvoe_element_from_list(c, 1)
    print("elemtn at index 1 must be deleted, now list c  : ", c)  # so does a

    lst = ["a", "b", "c"]
    lst = lst[1:]
    print("tail of lst :", lst)


demo_list_element_access()
# demo_list_operations()
# demo_list_operations_ex()
# demo_string_list_of_char_comparison()
