def ternary_op(condition):
    x = 100 if condition else 0
    print(x)

def demo_ternary_op():
    ternary_op(True)
    ternary_op(False)

def demo_tricks_ex():
    demo_ternary_op()


if __name__ == "__main__" :
    demo_tricks_ex()
