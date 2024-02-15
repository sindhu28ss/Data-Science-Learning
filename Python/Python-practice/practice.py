
import numpy as np



''''Given a list of labels [2, 0, 1, 2], encode it into one-hot vectors'''

a = [2,0,1,2]
print(np.max(a))
n_values = np.max(a) + 1
print(n_values)
one_hot = np.eye(n_values)[a]
print(one_hot)

import numpy as np
y = [2,0,1,2] # we have 3 differnet classes
print(len(y))
y_oh=np.eye(len(y))[np.array(y),:]
print(np.eye(len(y)))
print(y_oh)

a=np.eye(4)
print(a)
# one hot encoding a list, using multidimensional np index
import numpy as np
y=[1,2,3,4,1,0] # so we have 5 differnet classes
y_oh=np.eye(len(y))[np.array(y),:] # the first row of y_oh is the second row, all column.
                                    #  the second row in the y_oh is the third row, all column.
'''
We can say this as

y_oh=np.eye(len(y))[1,:] # the first row of y_oh is the second row, all column.
y_oh=np.eye(len(y))[2,:]
y_oh=np.eye(len(y))[3,:]
y_oh=np.eye(len(y))[4,:]
y_oh=np.eye(len(y))[1,:]
y_oh=np.eye(len(y))[0,:]

'''                     
print(np.eye(len(y)))
print(y_oh)


'''
the y_oh is
[[0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]
 [0. 1. 0. 0. 0.]
 [1. 0. 0. 0. 0.]]
'''  
#---------------------------------------------------------------------------

import numpy as np
y = [2,0,1,2] # we have 3 differnet classes
print(len(y))
y_oh=np.eye(len(y))[np.array(y),:-1]
print(np.eye(len(y)))
print(y_oh)














