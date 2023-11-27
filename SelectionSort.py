#The idea of selection sort is --> 

import numpy as np
arr = np.array([5,6,3,8,2])

for i in range(len(arr)-1):

    min= arr[i]
    idx = 0
    for j in range(i+1,len(arr)):
      
        
        if arr[j]<min:
            min = arr[j]
            idx = j
    arr[i],arr[idx]=min,arr[i]
print(arr)


#Sorting With Recursion
def selectionSort(arr):
    
    def subFun(min=arr[0],j=0,idx=0):
        if j==len(arr):
            return min,idx
        if arr[j]<min:
            min = arr[j]
            idx = j
       
        return subFun(min,j+1,idx)
        
            
        
    def mainFun(i=0):
        min = arr[i]    
        if i==len(arr)-1:
            return 0

        main =subFun(min,i+1)
        arr[i],arr[main[1]]=main[0],arr[i]
        mainFun(i+1)
        
    mainFun(0)
    return arr
        
    
        
    
    
arr1 = [5,6,3,8,2]
print(selectionSort(arr1))
