#check the factors
num=int(input("enter the number here:" ))
n=num
result=[]
for i in range(1,n+1):
    if n%i==0:
        result.append(i)
print(result)