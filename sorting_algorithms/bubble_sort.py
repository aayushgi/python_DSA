"""
Bubble Sort me do adjacent (saath-saath wale) elements ko compare kiya jata hai.

Agar order galat hai to swap kar do.
Ye process baar-baar repeat hota hai.
Har pass ke baad sabse bada element end me chala jata hai, bilkul bubble ki tarah upar uthne jaisa
"""

nums=[5,7,8,4,1,6,9,2]
def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
    
print(bubble_sort(nums))
