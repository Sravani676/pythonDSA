'''
Python DSA - Linear search
'''

class Solution:
    def linearSearch(self,Arr,target):
        if len(Arr) == 0:
            return -1
        for i in range(len(Arr)):
            if Arr[i] == target:
                return True
        return False
