# A tuple is a sequence of values. The values can be any type, and they are indexed by
# integers, so in that respect tuples are a lot like lists. The important difference is that
# tuples are immutable.

# zip is a built-in function that takes two or more sequences and “zips” them into a list
# of tuples where each tuple contains one element from each sequence. In Python 3, zip
# returns an iterator of tuples, but for most purposes, an iterator behaves like a list.

# tuple supports functions such as sort, compare operators(compares begining to end)


def demo_tuple_creation():
    empty_tuple = tuple()
    print("empty tuple -> ", empty_tuple)

    t = "a", "b", "c", "d", "e"
    print("tuple from values -> ", t)

    # or represent it using (better)
    t1 = ("a", "b", "c", "d", "e")
    print("tuple from values -> ", t1)

    # string to tuple elements
    t2 = tuple("abrakadabra")
    print("tuple elements from t2 -> ", t2) # it allows duplicates as well

    # access method is same as list i.e. 0 based l;
    print("t2[0] -> {}\nt2[3:6] -> {}".format(t2[0], t2[3:6]))

    # you can not modify tuple elements but can replace tuple
    #t3 = t2[0] + t2[3:6] # not working, says can not concatanate
    t2 = ("A",) + t2[3:6] # please do notice , after "A"
    print("relaced tuple(t2) - > ", t2)


def demo_tuple_operations():

    # tpl = (10,20,"Hello",20.5) #  will be error
    tpl = (10, 20, 20.5)
    print("Min of Tuple : ", min(tpl))  # will print 10
    print("Max of Tuple : ", max(tpl))  # will print 20.5
    print("Len of Tuple : ", len(tpl))  # will print 3

    lst = [10, 20, 30]
    tpl = tuple(lst)
    print("Tuple from list : ", tpl)

    a, b = 3, 5
    print("a = {}, b = {}".format(a, b))

    # c , d = 1,23,45 # error, too many parameters

    b, a = a, b
    print("a = {}, b = {}".format(a, b))

    username, service_provider = "abc.def@gmail.com".split("@")
    print("username = {},service_provider = {}".format(username, service_provider))


# def tuple_as_function_arg(*t): # pass tuple variable as *t or pass scattered value of tuple
#    print(t)


def tuple_as_function_arg(
    t,
):  # it will take only tuple variables not scattered values of tuple
    print(t)


def demo_tuple_as_function_arg():
    # tuple_as_function_arg(3,4,5)
    t = (3, 4, 5)
    tuple_as_function_arg(t)  # outputs ((3, 4, 5),)
    # tuple_as_function_arg(*t) # outputs (3, 4, 5)


def tuple_as_return_value():
    return (1, 2, 3)


def demo_tuple_as_return_value():
    t = tuple_as_return_value()
    print(t)


def demo_tuple_list():
    s = "abcd"
    l = [1, 2, 3, 4]
    t = zip(s, l)
    t = list(t)
    # print("Zipped tuple from string & list -> ", *t) # works, converts to tuple
    # print("Zipped tuple from string & list -> ", list(t)) # works, converts to list
    # print("Zipped tuple from string & list -> ", set(t)) # works, converts to
    for c, n in t:
        print(c, n)

    # from tuples to tuples of participants
    cs, ns = zip(*t)
    print("chars = {}, numbers = {}".format(cs, ns))


def demo_tuple_dictionary():
    print("Dictionary to tuples, items() gives list of tuples")
    d = {"a": 1, "b": 2, "c": 3}
    # l =  list(d.items())
    # print(l)
    for c, n in d.items():
        print(c, n)

    print("Even you can convert list of tuples to dictionary")
    lst = [(2, 4), (3, 9), (4, 16)]
    d = dict(lst)
    for c, n in d.items():
        print(c, n)

    # in zip if containers have differnet size, it zips for minimun number sized container
    # in below example 25 & 36 will be ignored from second list
    print("As zip gives list of tuples we can init dictionary from zip of containers")
    d = dict(zip("abc", [4, 9, 16, 25, 36]))
    for c, n in d.items():
        print(c, n)


# DEMOS
if __name__ == "__main__" :
    demo_tuple_creation()
    # demo_tuple_operations()
    # demo_tuple_as_function_arg()
    # demo_tuple_as_return_value()
    # demo_tuple_list()
    # demo_tuple_dictionary()
