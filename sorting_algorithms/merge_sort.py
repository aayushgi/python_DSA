
"""
Step-1
[8, 3, 5, 1]

↓

[8, 3]     [5, 1]

↓

[8] [3]    [5] [1]

step-2
[8] + [3]

Compare:

8 vs 3

3 chhota hai → pehle aayega

Result:

[3, 8]

step-3
[5] + [1]

↓

[1, 5]

final merge
[3, 8] + [1, 5]

Compare:

3 vs 1 → 1
3 vs 5 → 3
8 vs 5 → 5
8 bacha → 8

Final:

[1, 3, 5, 8]


Note: Merge Sort me hamesha while use karte hain.

"""
#this is for murge of two sorted arrays
left=[1,2,3,4]
right=[1,1,3,4,5,6,7]
def merge(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
            
    while i<n:
        result.append(left[i])
        i=i+1
    while j<m:
        result.append(right[j])
        j=j+1
    return(result)
print("here is the murged sorted array",merge(left,right))