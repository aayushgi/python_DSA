# Min and Max in Array
# Solved
# Difficulty: BasicAccuracy: 68.55%Submissions: 564K+Points: 1Average Time: 10m
# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

# Examples:

# Input: arr[] = [1, 4, 3, 5, 8, 6]
# Output: [1, 8]
# Explanation: minimum and maximum elements of array are 1 and 8.
# Input: arr[] = [12, 3, 15, 7, 9]
# Output: [3, 15]
# Explanation: minimum and maximum element of array are 3 and 15.

class Solution:
    def getMinMax(self, arr):
        # code here
        if len(arr)==1:
            return [arr[0],arr[0]]
            
        if arr[0]>arr[1]:
            max=arr[0]
            min=arr[1]
        else:
            min=arr[0]
            max=arr[1]
        for i in range(2,len(arr)):
            if arr[i]>max:
                max=arr[i]
            elif arr[i]<min:
                min=arr[i]
        return[min,max]
print(Solution().getMinMax([1, 4, 3, 5, 8, 6]))
