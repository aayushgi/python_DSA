#find the sum of max and min in an array
n=5
a=[-1,2,3,4,5]
def sum_of_max_and_min(n,a):
    if n==1:
        return a[0]
    if a[0]>a[1]:
        max=a[0]
        min=a[1]
    else:
        min=a[0]
        max=a[1]
    for i in range(2,n):
        if a[i]>max:
            max=a[i]
        elif a[i]<min:
            min=a[i]
    return max+min
print(sum_of_max_and_min(n,a))