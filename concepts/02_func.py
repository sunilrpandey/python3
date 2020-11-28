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


demo_math()

msg = "\nfunc being re-used, called two times in one func"
reuse_fun(msg)

pass_func_as_arg_toprint(func_with_msg, "Func as arg is being used to print")
