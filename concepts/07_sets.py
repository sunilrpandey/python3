# unordered collection of unique element
def demo_sets_creation():

    # empty set
    n1 = {}
    print(n1)

    # simply int set
    n = {3, 5, 7, 4}
    print(n)

    # in/not in for set
    print(5 in n)
    print(10 in n)
    print(17 not in n)

    s1 = set("test")
    print("s1 (test) -> ", s1)

    s2 = set("Taste")
    print("s2 (Taste) -> ", s2)

    print("s1 - s2 -> ", s1 - s2)  # in s1 but not in s2
    print("s2 - s1 -> ", s2 - s1)  # in s2 but not in s1
    print("s1 | s2 -> ", s1 | s2)  # in s1 or s2
    print("s1 & s2 -> ", s1 & s2)  # both in s1 and s2
    print("s1 ^ s2 -> ", s1 ^ s2)  # in s1 or s2 but not in both


demo_sets_creation()
