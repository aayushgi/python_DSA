#more optimal solution than other 
num=int(input("enter the number here:"))
n=num
result=[]
for i in range(1,n//2):#half of that number by which they dont have to call all the range they call only half of the number 
    if n%i==0:
        result.append(i)

result.append(num)
print(result)