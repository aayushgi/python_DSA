# this program is about selection sort
"""
Selection Sort ek algorithm hai jo har round me sabse chhota element (minimum) dhoondhta hai aur usko uski correct position par rakh deta hai.
Yeh process tab tak repeat hota hai jab tak poori array sort na ho jaye.


it would be in ascending order

"""

num=[5,7,8,4,1,6,9,2]
def selection_sorth(num):
    n=len(num)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if num[j]<num[min_index]:
                min_index=j 
                
        num[i],num[min_index]=num[min_index],num[i]
    return num
    
print(selection_sorth(num))