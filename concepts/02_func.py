import math

print(math)


def demo_math():
    print("Circumference of a circle is 2 * pi * r, so calculate for r = 2")
    print("Circumference : ", 2 * math.pi * 2)


def reuse_fun(message):
    print(message)
    demo_math()
    demo_math()


def func_with_msg(msg):
    print(msg)


def pass_func_as_arg_toprint(f, msg):
    f(msg)


def demo_reuse_funcs():
    msg = "\nfunc being re-used, called two times in one func"
    reuse_fun(msg)


def demo_join_list_of_string():
    lst_of_str = ["this", "is", "complete", "string"]
    complete_str = " ".join(str for str in lst_of_str)
    print(complete_str)


if __name__ == "__main__":
    # demo_math()
    # demo_reuse_funcs()
    # pass_func_as_arg_toprint(func_with_msg, "Func as arg is being used to print")
    demo_join_list_of_string()
