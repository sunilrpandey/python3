import math
# function param order : formal arg, *args,default,**kwargs
# #args as name does not matter
# print(math)
# **kwargs for it keys should be string only not in // need to confirm #TODO


def demo_math():
    print("Circumference of a circle is 2 * pi * r, so calculate for r = 2")
    print("Circumference : ", 2 * math.pi * 2)


def reuse_fun(message):
    print(message)
    demo_math()
    demo_math()


def func_with_msg(msg):
    print(msg)


def demo_pass_func_as_arg_toprint(f, msg):
    f(msg)


def demo_reuse_funcs():
    msg = "\nfunc being re-used, called two times in one func"
    reuse_fun(msg)


def demo_join_list_of_string():
    lst_of_str = ["this", "is", "complete", "string"]
    complete_str = " ".join(str for str in lst_of_str)
    print(complete_str)


def print_var_args(*args):
    for i in args:
        print(i, end="  ")
    print()

def print_var_args_with_formal_args(msg, *args):

    print("Demo: format message with var args")
    print(msg)    
    for i in args:
        print(i, end="  ")
    print()

def print_key_value_of_variable_length(**kwargs):
    '''
    similar to var args list, its actually var arg dict
    '''
    for k,v in kwargs.items():
        print("{}-{}".format(k,v), end=" , ")

def print_default_arg1(arg="hello"):
    print("Default arg : ", arg)

def demo_func_with_var_args():
    print_default_arg1()
    print_var_args(2,"one",23.5)
    print_var_args("Hello Data Types : ", 2,"one",23.5,[1,2,3],{1:"one",2:"two"},(4,5,6))
    print_key_value_of_variable_length(arg1="one", arg2="two")

def print_vals(arg1, arg2, arg3):
    print("Printing values : {}-{}-{}".format(arg1,arg2,arg3))

def demo_unpack_func_for_Containers():
    print("Unpack list..")
    print("print list using func with total number of params")
    lst = [1,"one",2.5]
    print_vals(*lst)

    print("User var arg version if you are not sure about number element in list")
    lst = [1,"one",2.5,[2,3,4],"hello"]    
    print_var_args(*lst)

    print("Unpack tuples..")
    print("print tuple using func with total number of params")
    tpl = (1,"one",2.5)
    print_vals(*tpl)

    print("User var arg version if you are not sure about number element in tuple")
    tpl = [1,"one",2.5,(2,3,4),"hello"]    
    print_var_args(*tpl)
    
    print("Unpack dictionary..")
    d = {'1':"one",'2':"two"}
    print_key_value_of_variable_length(**d)
    





    
if __name__ == "__main__":
    # demo_math()
    # demo_reuse_funcs()
    # demo_pass_func_as_arg_toprint(func_with_msg, "Func as arg is being used to print")
    #demo_join_list_of_string()
    demo_func_with_var_args()

    #demo_unpack_func_for_Containers()

