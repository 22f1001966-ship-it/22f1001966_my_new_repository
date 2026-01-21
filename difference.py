import numpy as np

#create a tuple
my_array1 = np.array([1,2,3,7,9])
my_array2 = np.array([4,5,6,7,8])
#calculate the difference of a and b in the tuple
array_difference = np.subtract(my_array2, my_array1)

print("The original array1 and array2: \n ", my_array1 ,"\n ",my_array2)
print("The difference of array2 and array1 : \n ", array_difference)