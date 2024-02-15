# numpy is a library for scientific computing in Python. It provides a high-performance multidimensional array object.
# it is very convinient to do linear algebra with numpy arrays

import numpy as np # without this line, the following won't work, if you only say import numpy,
 # you will have to call the numpy name afterwards, 
 # this is usually used for shortening the programming or to avoid common names.


# An array is a data structure, which can store a fixed-size collection of elements of the same data type
# List is used to collect items that usually consist of elements of multiple data types.
# An array is also a vital component that collects several items of the same data type. 
## Compared to list, array is much more efficient in terms of computation speed.

# defining one dimension array
array1=np.array([1,2,3,4,5,6])
print(array1)

# defining two dimensional array, you can see this as a matrix
array2=np.array([[1,2,3],[3,2,1]])
print(array2)

# shape of array
print(array2.shape)

# generate zero arrays of some array's shape, usually used for initialization
print(np.zeros(array2.shape))
print(np.zeros(3)) #1D
print(np.zeros((3,3))) #2D

# create identity matrix
array3=np.eye(4) # 4 is the size of the identity matrix
print(array3)

# most np functions are elementwise
x = np.array([[1, 2, 3],[4,5,6]])
print(x)
print(np.exp(x))
print(np.sqrt(x))
print(1/x)

#------------------------------------------------------------------
'''
1. Create an array of integers from 1 to 10.
2. Create a 3x3 matrix with values ranging from 0 to 8.
3. Create a 5x5 identity matrix.

'''
arr1=np.array(range(1,11))
print(arr1)

arr1=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1)

arr2=np.array([[0,1,2],
               [3,4,5],
               [6,7,8]])
print(arr2)

arr3=np.eye(5)
print(arr3)

#------------------------------------------------------------------

# broadcasting
array3=np.array([[1,2,3],[3,2,1]])
print(array3)
print(array3+1) # 1 is added to every elementin the array3
print(array3+np.array([1,2,3]).reshape(1,3)) # 1,2,3 is converted into a 1 by 3 array, and added to each row of array 3
print(array3+np.array([1,2]).reshape(2,1)) # 1,2 is converted into a 2 by 1 array, and added to each column of array3

np.array([1,2,3]).reshape(1,3)

# taking advantage of np library element calculation in defining functions

import numpy as np
import math

# function using math library
def sigmoid1(x):
   
    s = 1/(1+math.exp(-x))
    
    return s

#function using np library
def sigmoid2(x):
   
    s = 1/(1+np.exp(-x))
    
    return s

print(sigmoid1(3))
print(sigmoid1(np.array([[1,2,3],[4,5,6]])))

print(sigmoid2(3))
print(sigmoid2(np.array([[1,2,3],[4,5,6]])))

#----------------------------------------------------------------

# degenerate array
import numpy as np
x=np.array([1,2,3])
print(x.shape) # you have no idea whether it is a row array or column array

# you better reshape
x1= x.reshape(1,3)
print(x1)
print(x1.shape)

x2= x.reshape(3,1)
print(x2)
print(x2.shape)

'''
Add the vector [1, 1, 1] to each row of a matrix of shape (3, 3) filled with values of 2.
'''
arr4=np.array([[2,2,2],[2,2,2],[2,2,2]])
print(arr4)
print(arr4+np.array([1,1,1]))

#------------------------------------------------------------------
# np array subscripting
x = np.array([[1, 2, 3],[4,5,6]])
print(x)
x.shape
print(x[:,0]) # first column, index starts from 0
print(x[1,2]) # the second row, the third column
print(x[:,1:3]) # first column, the second and third column, note 1:3 means 1 and 2 (1<=x <3)


# higher dimensional np array
x=np.array([[[1,2,3],
             [4,5,6]],

            [[0,1,2],
             [3,4,5]],
             
            [[-1,0,1],
             [2,3,4]]])

print(x)
print(x.shape)
print(x[:,0,:])
print(x[:,0,:].shape)
print(x[:,:1,:])
print(x[:,:1,:].shape)
print(x[:,:2,:]) # the original array


print(x[:,:,:0])
print(x[:,:,:2]) 
print(x[:,:,:3]) # the original array

print(x[:,:,0])

#-----------------------------------------------------------------
# transpose
b=np.array([[1,2],
            [3,4],
            [5,6]])
print(b)
print(b.T)

#----------------------------------------------------------------

# matrix multiplication
import numpy as np

b=np.array([[1,2],
            [3,4],
            [5,6]]
		  ) # 3 x 2 matrix
b.shape

c=np.array([[1,2,3],
            [4,5,6]]) # 2 x 3 matrix
c.shape
print(c)

print(b*c) # this is element wise multiplication, cannot be done here 
# but the star * means element multiplication, 
# the two matrix joining the * operation must be the same shape.
# the following three calculations has the same result

print(np.matmul(b,c)) # 3 x 2 matrix multiplied by 2 x 3 matrix = 3 x 3 matrix
print(np.dot(b,c)) # np.matmul can be treated as the same as the np.dot
print(b@c) # also np.matmul(b,c) = b@c

print(np.matmul(c,b)) # the sequence matters # 2 x 3 matrix multiplied by 3 x 2 matrix = 2 x 2 matrix

#----------------------------------------------------------------------------------------------------------------------
          
import numpy as np
x=np.array([[1,2,3]])
print(x.shape)
y=np.array([[3,2,1]])
print(y.shape)
print(x*y)
print(x*y.T) # x becomes three rows of [1,2,3], and y becomes three columns of [3,2,1]

# convert from list to array
list1 = [1, 7, 0, 6, 2, 5, 6]
arr = np.array(list1)
print(arr)
print(arr.shape)

list2 = [[1, 2, 3], [4, 5, 6]]
arr2=np.array(list2)
print(arr2)
print(arr2.shape)
#------------------------------------------------------------------

# array flatten - returns a 1D array
#reshape(-1)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.flatten())
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.reshape(-1))


# multidimentional flatten 
x=np.array([[[1,2,3],
             [4,5,6]],

            [[0,1,2],
             [3,4,5]],
             
            [[-1,0,1],
             [2,3,4]]])
x.shape
print(x)
print(x.reshape(1,2,9)) # when doing flatten like this, it arranges the numbers in the original array sequentially
                         # as we have 18 elements, we have to match the number for reshaping array
# let's do the reshaping manually
# 1. flatten original sequentially
flattened=[]
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        for k in range(x.shape[2]):
            flattened.append(x[i,j,k])
print(flattened)


# 2. reshaping
result=np.zeros((2,9))
print(result)
idx=0
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        result[i,j] = flattened[idx]
        idx+=1
print(result) # this result should be exactly the same as print(x.reshape(-1,2,9))

#------------------------------------------------------------------
# remove redundant dimension

from numpy import zeros
x=zeros((10,10,1))
y=x[:,:,0]
print(y.shape)
print(x) # there is only one column on each slice
print(y)

# add one dimension
from numpy import zeros, newaxis
x=zeros((10,10))
print(x)
y=x[:,:,newaxis]
print(y.shape)
print(x)
print(y)

# keep dimension
# np max
import numpy as np
data = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.1, 0.2, 0.3, 0.4, 0.5, 0.6]).reshape((2,3,2))
print(data)
print(np.max(data,axis=1,keepdims=True)) #  we calculate the max along the axis 1, 
                                        # which is the second axis. For each floor, 
                                        # for each column, we find the max value across rows

# now let's do it manually here so you have a better idea
result = np.zeros((2,1,2)) # when finding the maximum on the axis 1, the axis 1 dimension size is reduced 
                            # from 3 to 1 (only the max value is kept in that dimension)
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        for k in range(result.shape[2]):
            result[i,j,k] = max(data[i,:,k]) 
print(result)

print(np.max(data,axis=1,keepdims=True).shape)
print(np.max(data,axis=1,keepdims=True))

print(np.max(data,axis=1,keepdims=False).shape)
print(np.max(data,axis=1,keepdims=False))

# np sum, very similar to np max
import numpy as np
data = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.1, 0.2, 0.3, 0.4, 0.5, 0.6]).reshape((2,3,2))
print(data)
print(np.sum(data,axis=1,keepdims=True))
print(np.sum(data,axis=1,keepdims=True).shape)
print(np.sum(data,axis=1,keepdims=False))
print(np.sum(data,axis=1,keepdims=False).shape)

# normalize only across one selected axis with np
import numpy as np
data = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.1, 0.2, 0.3, 0.4, 0.5, 0.6]).reshape((2,3,2))
print(data)
themax=np.max(data,axis=1,keepdims=True) # shape (2,1,2)
themin=np.min(data,axis=1,keepdims=True) # shape (2,1,2)
normalized=(data-themin)/(themax-themin) 
print(normalized)
normalized.shape

# multidimensional np index
import numpy as np
x=np.array(range(1,17)).reshape(4,4)
print(x)
index1=np.array([0,1,2,3])
index2=np.array([1,0,1,0])
print(x[index1,index2]) # the first number is row 0 and column 1, the second number is row 1 column 0,
                        # the third number is row 2 column 1, the last number is row 3 column 0

# compare two np array
import numpy as np
x1=np.array([1,2,3,4])
x2=np.array([2,2,2,2])
print(x1==x2)
print(np.sum(x1==x2)) # true is 1 and false is zero

# one hot encoding a list, using multidimensional np index
import numpy as np
y=[1,2,3,4,1,0] # so we have 5 differnet classes
y_oh=np.eye(len(y))[np.array(y),:] # the first row of y_oh is the second row, all column.
                                   #  the second row in the y_oh is the third row, all column.
print(np.eye(len(y)))
print(y_oh)                                  
'''
We can say this as

y_oh=np.eye(len(y))[1,:] # the first row of y_oh is the second row, all column.
y_oh=np.eye(len(y))[2,:]
y_oh=np.eye(len(y))[3,:]
y_oh=np.eye(len(y))[4,:]
y_oh=np.eye(len(y))[1,:]
y_oh=np.eye(len(y))[0,:]

'''
''''Given a list of labels [2, 0, 1, 2], encode it into one-hot vectors'''
                     
y = [2,0,1,2] # we have 3 differnet classes
y_oh=np.eye(3)[np.array(y),:]
print(y_oh)

#--------------------------------------------------------------------------------------------------------------------

# vectorization with numpy can dramatically speed up calculation, expecially when there are nested iterations.

# first use plain iterations
# 1. inner product (32 ms)
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

tic = time.process_time() # used to calculate cpu time, sleep time is not counted.

ctr = 0
while ctr < 10000: 
    
    dot = 0
    for i in range(len(x1)):
        dot += x1[i] * x2[i]
    ctr += 1
    
toc = time.process_time()

print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

# 2. element-wise multiplication (46 ms)
import numpy as np
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

tic = time.process_time()

ctr = 0
while ctr < 10000:
    mul = np.zeros(len(x1))
    
    for i in range(len(x1)):
        mul[i] = x1[i] * x2[i]
        
    ctr += 1
    
toc = time.process_time()

print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")


# 3. outer product (632 ms)
import numpy as np
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

tic = time.process_time()

ctr = 0
while ctr < 10000:
    outer = np.zeros((len(x1), len(x2))) # we create a len(x1)*len(x2) matrix with only zeros
    
    for i in range(len(x1)):
        for j in range(len(x2)):
            outer[i,j] = x1[i] * x2[j]
    
    ctr+=1
            
toc = time.process_time()
print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")


# use numpy vectorization
# 1. inner product (78 ms)
import numpy as np 
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

tic = time.process_time()

ctr = 0
while ctr < 10000:    
    dot = np.dot(x1,x2)
    ctr += 1
toc = time.process_time()
print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")


# 2. element wise multiplication (78 ms)
import numpy as np 
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

tic = time.process_time()

ctr = 0
while ctr < 10000:    
    mul= np.multiply(x1,x2)
    ctr += 1
toc = time.process_time()

print(mul)
print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

# 3. outer product (78 ms)
import numpy as np 
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

tic = time.process_time()

ctr = 0
while ctr < 10000:    
    outer = np.outer(x1,x2)
    ctr += 1
toc = time.process_time()

print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

#-----------------------------------------------------------------------------------------------------

# generating random numbers using numpy

from numpy import random
x = random.randint(10,20) # random int from 10 to 20
print(x)
x = random.rand() # random 0-1 float
print(x)
x=random.randint(10,20, size=(5)) # 5 random int from 10 to 20
print(x)
x=random.randint(10,20, size=(3,5)) # 3 by 5 random int from 10 to 20
print(x)
x = random.rand(3, 5) # random floats
print(x)

#-----------------------------------------------------------------------------------

# swapping axis
# it's like flipping the cube, row becomes column, deepth becomes row.....

x = np.array([[1,2,3]])
y = np.swapaxes(x,0,1)
print(x)
print(y)

x = np.array([[[0,1,2],
               [2,3,3]],
              [[4,5,1],
               [6,7,5]]])
print(x)
print(x.shape)

y = np.swapaxes(x, 1, 2) # swap row and columns
print(y)
print(y.shape)

z = np.swapaxes(x, 2, 0) #swap column and dimensions
print(z)
print(z.shape)

w = np.swapaxes(x, 1, 0) #swap row and dimensions
print(w)
print(w.shape)

#-----------------------------------------------------------------
