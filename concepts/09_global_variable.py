# Learning : if you are updationg global variable you have to use declare it as global in that scope
# global : bring global x to local function when you want to update x which is in global scope, it will not affect local x if any declared
# in outer func definition,
# non local : is generally used when we have nested functions, we bring outer func' x in the scope, not the global one

gv = 12
mutable_gv = {1, 2, 3}
spam = "temp"

def update_global_variable():
    global gv  # required if modifying this value, not rquired if being used for reading purpose only
    print("gv -> ", gv)
    print("Updating gv to 120")
    gv = 120
    
    print(
        "global list -> ", mutable_gv
    )  # global is not required if it is mutable such as list, dictioanary and sets
    # mutable_gv.append(4)
    local_set = {4, 5}
    mutable_gv.update(local_set)    

def demo_scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
        #print(spam) # will print updated value here only

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

# x = "me"
def demo_global():
    #print(x) # errorlocal variable 'x' referenced before assignment due to confusion
    global x # it shoudl be declared before it can be used
    print(x)
    x = "local"
    print(x)

n = 20
def demo_non_local():
    n = 50

    def inner():
        # nonlocal n  #only in nested function
        global n  # this will not change value n, for global only not for the local n
        print(n)
        n = 100

    print(n)
    inner()
    print(n)


def demo_global_list_and_update():
    glb_list = globals();
    print("Global list : ", glb_list)
    glb_list['gv'] = 15 # gv should be string
    print("global gv = ", gv)




# demo_non_local()
# print(n)

def demo_update_global_vars():
    update_global_variable()
    print("updated gv -> ", gv)
    print("updated mutable_gv -> ", mutable_gv)

if __name__ == "__main__":
    # demo_update_global_vars()
    #demo_scope_test()
    #print("In global scope:", spam)
    # demo_global()
    #demo_non_local()
    demo_global_list_and_update()
