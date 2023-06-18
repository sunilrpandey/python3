from array import array
from cgi import print_arguments
from re import A
from string import printable
import numpy as np
# array add elements where as list appends for + operator
#print(numpy.__doc__)

def demoCompareListwithNumpyArray():
    print("Add sq and cub of first 3 numbers using list..")
    lst1 = list(range(1,4))
    lst2 = list(range(1,4))
    lst_sum = []
    print(lst1)
    print(lst2)
    for i in range(3):
        lst1[i] = lst1[i] ** 2
        lst2[i] = lst2[i] ** 3
        lst_sum.append(lst1[i] + lst2[i])
    
    print (lst_sum)

    print("Add sq and cub of first 3 numbers using array..")
    arr1 = np.arange(1,4) ** 2
    arr2 = np.arange(1,4) ** 3
    print (arr1 + arr2)

    print("more mathematical ops..")
    print(np.power(np.array([1,2,3]),4))
    print(np.array([1,2,3]) ** 4)
    sample_arr = np.array([1,2,3])
    print("\nNegative : \n",np.negative(sample_arr))
    print("\nExp : \n",np.exp(sample_arr))
    print("\nLog : \n",np.log(sample_arr))

def demoMultDimensionArray():
    x = np.arange(3)
    y = np.arange(3,6)
    z = np.arange(6,9)
    mult_arr = np.array([x,y,z],dtype=np.int16) # dtype is optional
    print(mult_arr) 
    print(mult_arr.shape)
    print(mult_arr[1,2])
    print(mult_arr[1])



    
    
def demoSlices():
    #slice [start stop step]
    a = np.arange(10,20)
    print(a[2:7])

    x = np.arange(18).reshape(3,2,3)
    print(x[1,:2,:1]) #0 is default
    print(x[1,...]) # 
    print(x[1,:2,:3:2]) # 0:3:2 means columns 0 to 3, but alternate one since step is 2
    
    comparison_operator = x > 5
    print(comparison_operator)

    print(x[comparison_operator]) # output is list of values
    print(x[x>5])# output is list of values
    print(x.max())
    print(x.min())

def demoFlatAndRvel():
    # ravel returns reference to array element whereas flatten array returns copy of the values
    x = np.arange(9).reshape(3,3)
    print(x)

    ravelled_arr = x.ravel()
    print("ravelled array : \n",ravelled_arr)
    ravelled_arr[4] = 444
    print("Array got modified: \n",x)

    flattened_arr = x.flatten()
    print("flattened array : \n", flattened_arr)
    flattened_arr[4] = 888
    print("Array not modifed : \n",x)

def demoTranspose():
    a = np.arange(9)
    a.shape = [3,3]
    print(a)
    print("Tranposed : \n",a.T)

    print(np.zeros((2,3),dtype = float)) # float is default
    print(np.ones((2,3),dtype = int))
    print(np.eye(3,dtype = int))
    print(np.random.rand(3,3))

def demoMatrxMultiplication():
    mat_a = np.matrix([0,3,5,5,5,2]).reshape(2,3) # array can also be used
    print(mat_a)
    
    mat_b = np.matrix([3,4,3,-2,4,-2]).reshape(3,2)
    print(mat_b)
    
    print("Mult : \n",mat_a * mat_b) 
    product = np.matmul(mat_a,mat_b)
    print("Mult using matmul: \n",product)

    



def demoHStack():
    x = np.arange(8).reshape(2,4)
    y = np.arange(2,12).reshape(2,5)
    print("x->\n",x,"\ny->\n",y)
    print("size of x-> ", x.shape)
    print("size of y -> ", y.shape)
    hxy = np.hstack((x,y))
    print(hxy)
    print(hxy.shape)
    print("Can do the same using concatenate method and axis as 1")
    hconcat_xy = np.concatenate((x,y),axis = 1)
    print(hconcat_xy)
    print(hconcat_xy.shape)
    colstack_xy = np.column_stack((x,y))
    print("Column stack is same as hstack except one dim array : \n", colstack_xy)
    print(colstack_xy == hxy)

    

def demoVStack():
    x = np.arange(8).reshape(4,2)
    y = np.arange(2,12).reshape(5,2)
    print("x->\n",x,"\ny->\n",y)
    print("size of x-> ", x.shape)
    print("size of y -> ", y.shape)
    vxy = np.vstack((x,y))
    print(vxy)
    print(vxy.shape)
    print("Can do the same using concatenate method and axis as 0")
    vconcat_xy = np.concatenate((x,y),axis = 0)
    print(vconcat_xy)
    print(vconcat_xy.shape)
    print(vxy == vconcat_xy)

def demoDepthStack():
    x = np.arange(4).reshape(2,2)
    y = x * 2
    print(x)
    print(y)
    print("\nDepth Stack adds 3rd dimention to 2 dim matrices\n")
    dxy = np.dstack((x,y))
    print(dxy)
    print("dxy size : ", dxy.shape)
    
def demoColStackVSHorizontalStack():
    print("demo : when column and horizontal stack differs")
    a = np.arange(4)
    print(a)
    b = a * 2
    print(b)
    hab = np.hstack((a,b))
    print(hab)

    colstack_ab = np.column_stack((a,b))
    print(colstack_ab)
    

if __name__ == "__main__":
    # demoCompareListwithNumpyArray()
    # demoMultDimensionArray()
    # demoSlices()
    # demoFlatAndRvel()
    # demoTranspose()
    # demoMatrxMultiplication()
    # demoHStack()
    # demoVStack()
    # demoDepthStack()
    demoColStackVSHorizontalStack()
    i = 2 