def take_more_than_one_input():
    # Enter one number
    num = input("Enter numbers : ")
    print(num)

    # Take more than one input
    num1, num2, name = input("Enter numbers : ").split()
    # if we add 12_13 and split("_"), it will be treated as two number 12 and 13
    print(num1)
    print(num2)
    print(name)


def put_conditions_in_list_and_check_all_or_any():

    # condition in a list and use any() or all()
    x = 10
    y = 23
    z = 5

    if x > 7 and y > 20 and z < 10:
        print("Condition met!!")

    conditions_all = [x > 7, y > 20, z < 10]
    if all(conditions_all):
        print("All test : Have put conditions in list")

    conditions_any = [x > 7, y > 20, z > 10]
    if any(conditions_any):
        print("Any test : Have put conditions in list")


def swap_vars():
    x = "first"
    y = "last"
    print(x, y)

    x, y = y, x
    print(f"Swapped : {x} {y}")


def remove_duplicates_from_list():
    a = [1, 1, 2, 78, 3, 4, 3, 3, 3, 5]
    print("List with duplicates : ", a)
    a = list(set(a))
    print("List with removed duplicates : ", a)


def most_repeated_from_list():
    a = [1, 1, 2, 3, 78, 3, 4, 3, 3, 3, 5]
    print("List with duplicates : ", a)
    most_freq_number = max(set(a), key=a.count)
    print("most repeated number : ", most_freq_number)


def multiple_statement_in_oneline_in_list():
    odd_squares = []
    for i in range(11):
        if i % 2:
            odd_squares.append(i ** 2)
    print(odd_squares)
    odd_squares_now = [i ** 2 for i in range(11) if i % 2 != 0]
    print(odd_squares_now)


def varible_arg_sum(*a):
    result = 0
    for i in a:
        result += i
    return result


def demo_variable_arg():
    print(varible_arg_sum(20, 40, 30))


def reverse_string():
    name = "first last"[::-1]
    print(name)


def check_if_palindrome(str):
    is_palindrome = str.find(str[::-1]) == 0
    print(is_palindrome)
    return is_palindrome

def demo_join_list_of_string():
    lst_of_str = ["this", "is", "complete", "string"]
    complete_str = " ".join(str for str in lst_of_str)
    print(complete_str)



def demo_tricks():
    # take_more_than_one_input()
    # put_conditions_in_list_and_check_all_or_any()
    # swap_vars()
    # remove_duplicates_from_list()
    # most_repeated_from_list()
    # multiple_statement_in_oneline_in_list()
    # demo_variable_arg()
    # reverse_string()
    # demo_join_list_of_string()
    check_if_palindrome("madam")


if __name__ == "__main__":
    demo_tricks()
