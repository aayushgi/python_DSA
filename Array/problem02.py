"""
second largest number in the array

    nums=[1, 8, 7, 56, -90]
    return karna hai 8
    there will be 3 solutions
        1.brute force
        
        
            isme siple sa sort kar lena hai 
            the last ke jo second palce per element hai usko returan kar dena hai 
            nums.sort()
            then return nums[-2]
            
        2.better solution
            isme do variable lenge 
            largest aur second largest
     
code for better solution            
"""

nums=[55,32,97,-55,45,32,88,21]
largest=float('-inf')
second_largest=float('-inf')
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
    
for i in range(0,n):
    if nums[i]>second_largest and nums[i]!=largest:
        second_largest=nums[i]
        
print(second_largest)


#time complexity do bar loop chala so n+n=>o(2n)=>o(n)
#space complexity=>o(1) we are not using any extra space