from derived import Derived


def demo_reusability():
    print("Demo to show how a base impl of a func can be used in derived class")
    d = Derived()

    d.fun_impl()
    d.common_fun()


if __name__ == "__main__":
    demo_reusability()
