# lambda x: x
# lambda x : x + 2


def basic_lambda_demo():
    n = (lambda x: x + 2)(3)
    print(n)

    add_three = lambda x: x + 3
    print(add_three(5))

    sqr_func = lambda x:x*x
    print("square of 15 : ", sqr_func(15))

    lst = ["this", "is" ,"best", "list"]
    list_displayer_lambda(lst)
    print()

def lambda_with_multiple_arg():
    mult_func = lambda x, y , z : x * y * z
    print("Mult of 3 4 5 : ", mult_func(3,4,5))

def list_displayer_lambda(lst):
    disp_lambda = lambda x : print(x, end= "  ")
    for elem in lst:
        disp_lambda(elem)


def lambda_with_conditional_statement():
    in_range_of_10_to_15 =  lambda x : True if (x >= 10 and x <= 15) else False

    print("Is in range of 10-15 : ", in_range_of_10_to_15(5))
    print("Is in range of 10-15 : ", in_range_of_10_to_15(15))
    print("Is in range of 10-15 : ", in_range_of_10_to_15(13))

    print("Without if/else...")
    in_range_of_10_to_15 =  lambda x : x >= 10 and x <= 15
    print("Is in range of 10-15 : ", in_range_of_10_to_15(5))
    print("Is in range of 10-15 : ", in_range_of_10_to_15(15))
    print("Is in range of 10-15 : ", in_range_of_10_to_15(13))

    cond_multipliar = lambda x : x*2 if x < 5 else (x*3 if x < 10 else x)
    print("4 -> ", cond_multipliar(4))
    print("7 -> ", cond_multipliar(7))
    print("14 -> ", cond_multipliar(14))




if __name__ == "__main__":
    #basic_lambda_demo()
    #lambda_with_multiple_arg()
    lambda_with_conditional_statement()
