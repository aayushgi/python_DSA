# this aalgo is about quick sort algorithm
"""
1.frist we have to choose the povit element from the array
    it wolud be the frist  element of trhe array
    we can also choose the last element of the array
    we can also choose the midde element of the array
    or we can choose any number from the array as a povit element

2.put povit element in the correct position in the array
3.put all the elements smaller than the povit element to the left of the povit element
4.put all the elements greater than the povit element to the right of the povit element
5.repeat the process for the left and right sub-arrays until the array is sorted    

"""
def quick_sort(nums):
    if len(nums)<=1:
        return nums
    pivot=nums[0]
    left=[x for x in nums[1:] if x < pivot]
    right=[x for x in nums[1:] if x >= pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)

nums=[8,3,5,1,1,5,3,5,9,67,3,46,89]
print("Original array:", nums)
print("Sorted array:", quick_sort(nums))

