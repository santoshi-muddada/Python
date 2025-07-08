

import array
my_array=array.array('i',[54,87,76,24,90,87,12,43,35])
sorted_array=my_array.tolist()
sorted_array.sort(reverse=False)
print("the second smallest number: ",sorted_array[1]) 
sorted_array.sort(reverse=True)
print("the second largest number: ",sorted_array[1])



