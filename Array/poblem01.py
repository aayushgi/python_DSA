"""
Largest in Array

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.



"""

nums=[1, 8, 7, 56, -90]
def largest_in_array(nums):
    largest=nums[0]
    n=len(nums)
    for i in range(0,n):
        largest=max(largest,nums[i])
        
    return largest

print("Original array:", nums)
print("Largest element in the array:", largest_in_array(nums))