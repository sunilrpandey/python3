# Learnings
# append/extend modifies the list whereas + operator creates new list
# slice also creates a new list

# Don’t forget that most list methods modifies the argument and return None . This is
# the opposite of the string methods, which return a new string and leave the original
# alone.

from collections import deque
from collections import Counter

def demo_list_create():
    lst = [] # empty list
    print(lst)

    lst = ["Hello"] * 5
    print(lst)

    lst = ["World" for i in range(5)]
    print(lst)


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
    print("Remove 400 if exists : ")
    if 400 in mylist:
        print("Deleting {}...".format(400))
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

    list4.append(3) # this does not return list
    print("append method updates itself but does not return list : ", list4)

    another_list = [4,5]
    list4.append(another_list) # will output [1,2,3,[4,5]] not [1,2,3,4,5]
    print("append adds whole list not individual elem : ", list4)
    
    lst_to_extend = [6,7]
    list4.extend(lst_to_extend) # this does not return list but adds 6, 7 to existing list make list4 = [1, 2, 3, [4, 5], 6, 7]
    print(list4)
    print("extend function updates itself but does not return list : ", list4.extend(list1))




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

def remove_mult_occur_from_list():
    l = [10,10,10,30,28,30,45,98]
    i = 10
    while i in l:
        l.remove(i)

    print(l)

#using list comprehension
def remove_items_from_list_list_comprehension(lst, item1, item2): 
    trimmed_list = [num for num in lst if num != item1 and num !=item2 ]
    return trimmed_list;

def remove_items_from_list_lambda(lst, item1, item2): 
    trimmed_list = list(filter(lambda num: num != item1 and num != item2, lst))
    return trimmed_list;

def demo_remove_items_from_list():

    print("Demo : Remove items using list comprehension..")
    l = [10,23,45,67,12,34,67]
    l = remove_items_from_list_list_comprehension(l,23,67)
    print(l)
    
    print("Demo : Remove items using lambda..")
    l = [10,23,45,67,12,34,67]
    l = remove_items_from_list_lambda(l,23,67)
    print(l)

def remove_first_list_item_using_deque(lst):
    q = deque(lst)
    q.popleft();
    return list(q)

def demo_remove_first_list_item_using_deque():
    l = [10,23,45,67,12,34,67]
    l = remove_first_list_item_using_deque(l)
    print(l)

def demo_remove_duplicates():
    print("Demo : Remove Duplicates from the list")
    print("...using Set")
    l = [10,23,45,67,45,12,67,34,67]
    l = list(set(l))
    print(l)

    print("...to perserve order of elements, use looping")
    l = [10,23,45,67,45,12,67,34,67]
    print("l[::-1] : ", l[::-1])
    unqlist = []
    for itm in l:
        if itm not in unqlist:
            unqlist.append(itm)
    print(unqlist)

def demo_get_indices_of_given_item():
    print("Demo : Get indices of given item")
    #using list comprehension
    l = [10,23,45,67,45,12,67,34,67]
    indices_list = [i for i in range(len(l)) if l[i] == 67]
    print(indices_list)

def divisible_by_13(num):
    return not num%13

def demo_check_if_any_number_divisible_by_13():

    print("Check if number divisible by 13 using any...")
    lst = [10,26,45,65,45,12,65,34,65]    
    result = any(divisible_by_13 for elem in lst)
    if result:
        print("Present!!")
    else:
        print("Not Present!!")

    # Using list comprehension
    print("Check if number divisible by 13 using list comprehension...")
    lst = [10,26,45,65,45,12,65,34,65]    
    indices_list = [i for i in range(len(lst)) if lst[i]%13 == 0]
    if(len(indices_list)):
        print("Number divisible by 13 present at loc :", indices_list)    
    else:
        print("Number divisible by 13 not present in given list")    
def demo_check_if_list1_subset_of_list2():
    l1 = [3,5,7]
    l2 = [1,3,5,7,9,11]
    present = all(elem in l2 for elem in l1)
    print("All present?? -> ", present)

    l1 = [3,5,7]
    l2 = [2,4,6,8,10]
    present = any(elem in l2 for elem in l1)
    print("Any Present?? -> ", present)

    l1 = [2,3,5,7]
    l2 = [2,4,6,8,10]
    present = any(elem in l2 for elem in l1)
    print("Any Present?? -> ", present)

def get_number_unique_items(lst):
    return len(list(set(lst)))

def demo_check_if_all_element_are_same():
    # l = [1] * 5
    l = [2,2,2,4]
    if get_number_unique_items(l) == 1:
        print("All element are same as list out of set has only one element")
    else:
        print("Different elements are present")

def comparator( tpl_item ) :
    return tpl_item[1]

def demo_sort_list_of_tuples_on_second_item():
    tpl_list = [("Two",2),("Three",3),("One",1)]
    print("Given list : ", tpl_list)
    
    #tpl_list.sort()
    print("Sorted list : ", tpl_list)
    
    use_lambda = 1
    if use_lambda:
        tpl_list.sort(key=comparator)
        print("Sorted list on second item (using lambda): ", tpl_list)
    else :
        tpl_list.sort(key=lambda elem: elem[1])
        print("Sorted list on second item (using func object): ", tpl_list)

def get_num_element_list(lst):
    count = 0
    for item in lst:
        if type(item) == list:
            count += get_num_element_list(item)
        else:
            count = count + 1

    return count




def demo_get_num_element_list():
    l = [1,2,3]
    num_elem = get_num_element_list(l)
    print("Total elem (Homo list):", num_elem)

    l = [1,2,[3,4,5],6,7]
    num_elem = get_num_element_list(l)
    print("Total elem (Hetro list):", num_elem)

    l = [[1,2],[3,4,5],[6,7,8,9]]
    num_elem = get_num_element_list(l)
    print("Total elem (2D list):", num_elem)

def apply_lambda(lmbda,lst):
    return sum(map(lmbda,lst))

def cond_dev_by_13(item):
    return item % 13 == 0 

def demo_get_conditional_num_elem_using_sum_map():
    lst = [10,26,45,65,45,12,65,34,65] 
    
    lmbda_odd = lambda x:x%2==1
    count = apply_lambda(lmbda_odd,lst) 
    print("Total odd in the list : {}".format(count))

    lmbda_devby_5 = lambda x:x%5==0
    count = apply_lambda(lmbda_devby_5,lst) 
    print("Total nums divided by 5 : {}".format(count))
    
    count = len([item for item in lst if lmbda_devby_5(item)])
    print("Total nums divided by 5 (using list comprehension) : {}".format(count))
    
    # total numbers divided by 13
    count = sum(cond_dev_by_13(item) for item in lst)
    print("Total nums divided by 13 : ", count)

def check_duplicates_compare_len_list_and_set(lst):
    return len(lst) != len(list(set(lst)))

def check_duplicates_using_dict(lst):
    dup_dict = dict()
    for elem in lst:
        if elem in dup_dict:
            dup_dict[elem] += 1
        else :
            dup_dict[elem] = 1

    dict_of_dup_only = {k:v for k,v in dup_dict.items() if v > 1}
    return len(dict_of_dup_only) > 0

    #or using iteration
    for k,v in dup_dict.items():
        if v > 1:
            return True

    return False  

def check_duplicates_using_freq_counter(lst):
    dup_dict = dict(Counter(lst))
    #print(dup_dict)
    #for k,v in dup_dict.items():
    dup_dict = {k:v for k,v in dup_dict.items() if v > 1}
    #print(dup_dict)
    return len(dup_dict) > 0
        



def demo_check_duplicates_in_list():
    lst = [10,26,45,65,45,12,65,34,65]
    #print("Have duplicates : ",check_duplicates_compare_len_list_and_set(lst))
    #print("Have duplicates : ",check_duplicates_using_dict(lst))
    print("Have duplicates : ",check_duplicates_using_freq_counter(lst))

def convert_list_to_string(lst, separator=' '):
    return separator.join(lst)

def demo_convert_list_to_string():
    lst = ["Honesty", "is", "the", "best", "policy"]
    lst_str = ' '.join(i for i in lst)
    print(lst_str)
    
    lst_str = convert_list_to_string(lst)
    print(lst_str)
    
    lst_str = convert_list_to_string(lst, "--")
    print(lst_str)
    
    lst = [10,26,45,65,45,12,65,34,65]
    lst_str = ','.join(str(elem) for elem in lst)
    print(lst_str)

    lst = ["Honesty", 1, "is", 5, "the", 9.5, "best", [3,4,5], "policy"]
    lst_str = ' '.join(str(elem) for elem in lst)
    print(lst_str)

def demo_convert_nested_list_to_flat_list():
    lst = [[1,2,3],[4,5,6],[7,8]] # will work only if it is 2d list not list of list and individual both
    flt_list = [j for i in lst for j in i]
    print(flt_list) 

    # use extend if it has both

if __name__ == "__main__":
    demo_list_create()
    demo_list_element_access()
    demo_list_operations()
    demo_list_operations_ex()
    demo_string_list_of_char_comparison()

    remove_mult_occur_from_list()
    demo_remove_items_from_list()
    demo_remove_first_list_item_using_deque()
    demo_remove_duplicates()

    demo_get_indices_of_given_item()
    demo_check_if_any_number_divisible_by_13()
    demo_check_if_list1_subset_of_list2()
    demo_check_if_all_element_are_same()
    demo_sort_list_of_tuples_on_second_item()

    demo_get_num_element_list()
    demo_get_conditional_num_elem_using_sum_map()
    demo_check_duplicates_in_list()
    demo_convert_list_to_string()

    demo_convert_nested_list_to_flat_list()