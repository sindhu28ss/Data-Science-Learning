# Numpy

import numpy as np

print(np.__version__)

#Create a NumPy ndarray Object
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
arr = np.array((1, 2, 3, 4, 5))
print(arr)

#Dimensions in Arrays
#A dimension in arrays is one level of array depth (nested arrays).
#nested array: are arrays that have arrays as their elements

#0-D Arrays
#0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
arr = np.array(42)
print(arr)

#1-D Arrays
#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

arr = np.array([1, 2, 3, 4, 5])
print(arr)

#2-D Arrays
#An array that has 1-D arrays as its elements is called a 2-D array.

arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
print(arr)

#3-D arrays
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.

arr = np.array([[[1, 2, 3], 
                 [4, 5, 6]], 
                [[1, 2, 3], 
                 [4, 5, 6]]])

print(arr)

#Check Number of Dimensions?
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(42)
print(a.ndim)

b = np.array([1, 2, 3, 4, 5])
print(b.ndim)

c = np.array([[1, 2, 3], 
              [4, 5, 6]])
print(c.ndim)

d = np.array([[[1, 2, 3], 
               [4, 5, 6]], 
              [[1, 2, 3], 
               [4, 5, 6]]])
print(d.ndim)

#Higher Dimensional Arrays
#An array can have any number of dimensions.
#When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

#-------------------------------------------------

#Access Array Elements
#Array indexing is the same as accessing an array element.
#The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

arr = np.array([1, 2, 3, 4])
print(arr[0])

#Access 2-D Arrays
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
#Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

#Access 3-D Arrays
#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

#Negative Indexing
#Use negative indexing to access an array from the end.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

#--------------------------------------------------------------------------

#Slicing arrays:
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
#If we don't pass start its considered 0
#If we don't pass end its considered length of array in that dimension
#If we don't pass step its considered 1

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Note: The result includes the start index, but excludes the end index.

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#Negative Slicing
#Use the minus operator to refer to an index from the end:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#Use the step value to determine the step of the slicing:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
    
#Return every other element from the entire array:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

#Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

#-------------------------------------------------
a[0],a[1]
a[0:] #beginning till end
a[1:3] # 1st index and 2nd index
a[1:-1] #1st index and last before index
a[::2] #gets every even
b[0],b[2],b[-1]
b[[0,2,-1]]

#Array types:

a
a.dtype
b
b.dtype
np.array([1,2,3,4], dtype=float)
c=np.array(['a','b','c'])
c.dtype
d=np.array([{'a':1},sys])
d.dtype

#Dimensions and shape

a=np.array([[1,2,3],[4,5,6]])
a.shape
a.ndim
a.size

b=np.array([
    [
    [12,11,10],
    [9,8,7],
    ],
    [
     [6,5,4],
     [3,2,1]
     ]
    ])

b
b.shape
b.ndim
b.size

c=np.array([
    [
      [10,11,12],
      [4,5,6],
    ],
    [
      [3,7,9]
    ]
  ])

c.dtype
c.size

#Indexing and slicing of matrices
#square matrix

a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
a[1]
a[1][0]
a[1,0]
a[0:2]
a[:,:2]
a[:2,:2]
a[:2,2:]
a[1]=np.array([10,10,10])
a
a[2]=99
a

#summary statistics
a=np.array([1,2,3,4])
a.sum()
a.mean()
a.std()
a.var()

a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

a.sum()
a.mean()
a.std()

a.sum(axis=0)
a.sum(axis=1)
a.sum(axis=2)

a.mean(axis=1)
a.std(axis=0)
a.std(axis=1)

#Broadcasting and vectorized operations
a=np.arange(4)
a
a+10 #10 added to each element
a*10 #10 multiplied to each element
a
a+=100 #100 added to each element
a

l=[0,1,2,3]
[i*10 for i in l] #10 multiplied for each element in l

a=np.arange(4)
a
b=np.array([10,10,10,10])
b
a+b
a*b

#Boolean arrays
a=np.arange(4)
a
a[[0,-1]] #1st & last element
a[[True,False,False,True]] #give values for true
a>=2 #gives >=2 values as True or false
a[a>=2] #gives >=2 values in array
a.mean()
a[a>a.mean()]

a[(a==0)|(a==1)]
a[(a<=2) & (a%2==0)]

a=np.random.randint(100,size=(3,3))
a
a[np.array([
    [True,False,True],
    [False,True,False],
    [True,False,True]
    ])]
a>30
a[a>30]

#Linear Algebra

a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])
b=np.array([
    [6,5],
    [4,3],
    [2,1]
    ])

a.dot(b)
a@b
b.T #Transpose
a
b.T@a
#---------------------------------------------------
#size of objects in memory
#int,floats
#An integer in python is >24 bytes
sys.getsizeof(1)

#Longs are even larger
sys.getsizeof(10**100)

#Numpy size is much smaller
np.dtype(int).itemsize
np.dtype(float).itemsize

#lists are even larger
#A one-element list
sys.getsizeof([1])

#An array of one element in Numpy
np.array([1]).nbytes

#And performance is also important
l=list(range(1000))
a=np.arange(1000)
%time np.sum(a**2)
%time sum([x**2 for x in l])









