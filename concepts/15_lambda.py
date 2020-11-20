#lambda x: x
#lambda x : x + 2

def basic_lambda_demo():
    n = (lambda x : x + 2)(3)
    print(n)

    add_three = lambda x : x + 3
    print(add_three(5))

def filter_list_of_numbers_for_odd_nums():
    # Program to filter out only the even items from a list
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: (x%2 != 0) , my_list))
    print("list of odd numbers : ", new_list)

if __name__ == "__main__" :
    basic_lambda_demo()
    filter_list_of_numbers_for_odd_nums()