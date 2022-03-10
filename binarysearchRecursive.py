def binarySearchRecursive(Arr,low,high,target):
    """
    :type Arr: list(Sorted)
    :type target : int 
    :rtype: int (Index of the target element)
    """
    if len(Arr) == 0:
        return -1
    while low <= high:
        mid = (low+high)//2
        if Arr[mid] == target:
            return mid
        elif Arr[mid] > target:
            return binarySearch(Arr,low,mid-1,target)
        else:
            return binarySearch(Arr,mid+1,high,target)
    return -1
