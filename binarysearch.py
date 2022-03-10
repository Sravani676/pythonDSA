'''
python Binary search
'''
class Solution:
    def binarySearch(self,Arr,target):
        """
        :type Arr: list(Sorted)
        :type target : int 
        :rtype: int (Index of the target element)
        """
        #checking if the input array is null
        if len(Arr) == 0:
            return -1
        
        #set the low and high index to start and end of the given list
        low, high = 0, len(Arr)-1
        
        #loop
        while low <= high:
            
            #set the index value of middle element to mid
            mid = (low+high)//2
            
            #checking if the target number is middle element
            if Arr[mid] == target:
                return mid
                
            #if the middle element is greater than the target element
            #then set the high to the first half of the list
            elif Arr[mid] > target:
                high = mid - 1 
            
            #if the middle element is less than the target element
            #then set the low to the second half of the list
            else:
                low = mid + 1
        
        #return -1 if the element is not found
        return -1
