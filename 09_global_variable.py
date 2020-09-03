# Learning : if you are updationg global variable you have to use declare it as global in that scope

gv = 12

mutable_gv = {1,2,3}

def update_global_variable() :
    global gv  # required if modifying this value, not rquired if being used for reading purpose only
    print("gv -> ", gv) 
    gv = 120
    print("updated gv to : ", gv) 

    print("global list -> ",mutable_gv) # global is not required if it is mutable such as list, dictioanary and sets 
    #mutable_gv.append(4)
    local_set = {4,5}
    mutable_gv.update(local_set)
    
def access_updated_global_variable() :
    print("updated gv -> ", gv) 
    print("updated mutable_gv -> ", mutable_gv) 

update_global_variable()
access_updated_global_variable()